#!/usr/bin/env python3
"""
CV Processing Module - Enhanced HR DSS
Module xử lý CV từ PDF và Image với OCR và Information Extraction
"""

import os
import re
import json
import logging
from typing import Dict, List, Optional, Tuple
from pathlib import Path
from datetime import datetime
import pandas as pd

# PDF Processing
try:
    import PyPDF2
    import pdfplumber
    HAS_PDF = True
except ImportError:
    HAS_PDF = False
    print("⚠ PDF libraries not installed. Run: pip install PyPDF2 pdfplumber")

# Image Processing & OCR
try:
    from PIL import Image
    import pytesseract
    import cv2
    import numpy as np
    HAS_OCR = True
except ImportError:
    HAS_OCR = False
    print("⚠ OCR libraries not installed. Run: pip install pillow pytesseract opencv-python")

# Text Processing
import spacy
try:
    nlp = spacy.load("en_core_web_sm")
    HAS_SPACY = True
except OSError:
    HAS_SPACY = False
    print("⚠ spaCy model not found. Run: python -m spacy download en_core_web_sm")
    nlp = None

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CVProcessor:
    """
    CV Processor - Xử lý CV từ PDF và Image
    """

    def __init__(self, upload_folder: str = "uploads/"):
        self.upload_folder = Path(upload_folder)
        self.upload_folder.mkdir(exist_ok=True)

        # Patterns for information extraction
        self.email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        self.experience_pattern = r'(\d+)\s*(?:\+?\s*)?(?:years?|yrs?)'

        # Skill keywords
        self.programming_skills = [
            'python', 'java', 'javascript', 'c++', 'c#', 'php', 'ruby', 'go', 'rust',
            'react', 'angular', 'vue', 'nodejs', 'django', 'flask', 'spring', 'laravel'
        ]

        self.data_science_skills = [
            'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'keras',
            'scikit-learn', 'pandas', 'numpy', 'matplotlib', 'seaborn', 'sql', 'nosql',
            'data analysis', 'statistics', 'data visualization', 'tableau', 'powerbi'
        ]

        self.devops_skills = [
            'docker', 'kubernetes', 'aws', 'azure', 'gcp', 'terraform', 'ansible',
            'jenkins', 'gitlab', 'ci/cd', 'microservices', 'linux', 'bash', 'python'
        ]

        self.design_skills = [
            'photoshop', 'illustrator', 'figma', 'sketch', 'adobe creative suite',
            'ui design', 'ux design', 'prototyping', 'wireframing', 'responsive design'
        ]

        self.project_management_skills = [
            'agile', 'scrum', 'kanban', 'pmp', 'project management', 'stakeholder management',
            'risk management', 'jira', 'confluence', 'team leadership', 'communication'
        ]

        # Education keywords
        self.education_keywords = [
            'phd', 'doctorate', 'master', 'm.sc', 'm.s', 'mba', 'bachelor', 'b.sc', 'b.s',
            'bachelor\'s', 'master\'s', 'associate', 'diploma', 'certificate', 'certification'
        ]

        logger.info("🔧 CV Processor initialized")

    def process_cv(self, file_path: str) -> Dict:
        """
        Xử lý CV từ file (PDF hoặc Image)

        Args:
            file_path (str): Đường dẫn đến file CV

        Returns:
            Dict: Thông tin trích xuất từ CV
        """
        try:
            file_path = Path(file_path)
            logger.info(f"📄 Processing CV: {file_path.name}")

            # Extract text from CV
            text = self._extract_text(file_path)

            if not text or len(text.strip()) < 50:
                logger.warning("⚠ Could not extract sufficient text from CV")
                return self._get_empty_result(file_path.name)

            # Extract information
            extracted_info = {
                'file_name': file_path.name,
                'file_type': file_path.suffix.lower(),
                'extracted_at': datetime.now().isoformat(),
                'raw_text': text
            }

            # Extract structured information
            extracted_info.update(self._extract_contact_info(text))
            extracted_info.update(self._extract_skills(text))
            extracted_info.update(self._extract_education(text))
            extracted_info.update(self._extract_experience(text))
            extracted_info.update(self._extract_projects(text))
            extracted_info.update(self._extract_certifications(text))
            extracted_info.update(self._extract_languages(text))

            logger.info(f"✅ Successfully processed CV: {file_path.name}")
            return extracted_info

        except Exception as e:
            logger.error(f"❌ Error processing CV {file_path}: {str(e)}")
            return self._get_empty_result(getattr(file_path, 'name', 'unknown'))

    def _extract_text(self, file_path: Path) -> str:
        """
        Trích xuất text từ file PDF hoặc Image
        """
        try:
            if file_path.suffix.lower() == '.pdf':
                return self._extract_from_pdf(file_path)
            elif file_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']:
                return self._extract_from_image(file_path)
            else:
                logger.warning(f"⚠ Unsupported file type: {file_path.suffix}")
                return ""
        except Exception as e:
            logger.error(f"❌ Error extracting text: {str(e)}")
            return ""

    def _extract_from_pdf(self, file_path: Path) -> str:
        """
        Trích xuất text từ PDF file
        """
        text = ""

        if not HAS_PDF:
            logger.warning("⚠ PDF libraries not available")
            return ""

        try:
            # Try pdfplumber first (better for tables and layout)
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
        except:
            try:
                # Fallback to PyPDF2
                with open(file_path, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    for page in pdf_reader.pages:
                        text += page.extract_text() + "\n"
            except Exception as e:
                logger.error(f"❌ Error reading PDF: {str(e)}")

        return text.strip()

    def _extract_from_image(self, file_path: Path) -> str:
        """
        Trích xuất text từ image file sử dụng OCR
        """
        if not HAS_OCR:
            logger.warning("⚠ OCR libraries not available")
            return ""

        try:
            # Preprocess image for better OCR
            image = cv2.imread(str(file_path))

            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Apply threshold to get binary image
            _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # Noise removal
            kernel = np.ones((1, 1), np.uint8)
            processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

            # Perform OCR
            text = pytesseract.image_to_string(processed, lang='eng')

            return text.strip()

        except Exception as e:
            logger.error(f"❌ Error performing OCR: {str(e)}")
            return ""

    def _extract_contact_info(self, text: str) -> Dict:
        """
        Trích xuất thông tin liên hệ
        """
        contact_info = {}

        # Email
        emails = re.findall(self.email_pattern, text, re.IGNORECASE)
        if emails:
            contact_info['email'] = emails[0]

        # Phone
        phones = re.findall(self.phone_pattern, text)
        if phones:
            contact_info['phone'] = phones[0]

        # Name (simplified - would need NLP for better accuracy)
        if HAS_SPACY:
            doc = nlp(text[:500])  # Check first 500 chars
            persons = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
            if persons:
                contact_info['name'] = persons[0]

        # LinkedIn profile
        linkedin_pattern = r'linkedin\.com/in/[\w-]+'
        linkedin = re.findall(linkedin_pattern, text, re.IGNORECASE)
        if linkedin:
            contact_info['linkedin'] = linkedin[0]

        # GitHub profile
        github_pattern = r'github\.com/[\w-]+'
        github = re.findall(github_pattern, text, re.IGNORECASE)
        if github:
            contact_info['github'] = github[0]

        return contact_info

    def _extract_skills(self, text: str) -> Dict:
        """
        Trích xuất kỹ năng từ text
        """
        text_lower = text.lower()

        found_skills = {
            'programming': [],
            'data_science': [],
            'devops': [],
            'design': [],
            'project_management': [],
            'other': []
        }

        # Programming skills
        for skill in self.programming_skills:
            if skill in text_lower:
                found_skills['programming'].append(skill)

        # Data science skills
        for skill in self.data_science_skills:
            if skill in text_lower:
                found_skills['data_science'].append(skill)

        # DevOps skills
        for skill in self.devops_skills:
            if skill in text_lower:
                found_skills['devops'].append(skill)

        # Design skills
        for skill in self.design_skills:
            if skill in text_lower:
                found_skills['design'].append(skill)

        # Project management skills
        for skill in self.project_management_skills:
            if skill in text_lower:
                found_skills['project_management'].append(skill)

        # Combine all skills
        all_skills = []
        for category, skills in found_skills.items():
            all_skills.extend(skills)

        return {
            'skills_by_category': found_skills,
            'all_skills': list(set(all_skills)),
            'skills_count': len(all_skills)
        }

    def _extract_education(self, text: str) -> Dict:
        """
        Trích xuất thông tin học vấn
        """
        text_lower = text.lower()
        education_info = {
            'highest_degree': None,
            'education_details': []
        }

        # Find education keywords
        degrees_found = []
        for keyword in self.education_keywords:
            if keyword in text_lower:
                degrees_found.append(keyword)

        if degrees_found:
            # Determine highest degree (simplified)
            if any(degree in ['phd', 'doctorate'] for degree in degrees_found):
                education_info['highest_degree'] = 'phd'
            elif any(degree in ['master', 'm.sc', 'm.s', 'mba'] for degree in degrees_found):
                education_info['highest_degree'] = 'master'
            elif any(degree in ['bachelor', 'b.sc', 'b.s', 'bachelor\'s'] for degree in degrees_found):
                education_info['highest_degree'] = 'bachelor'
            elif any(degree in ['associate'] for degree in degrees_found):
                education_info['highest_degree'] = 'associate'
            else:
                education_info['highest_degree'] = 'high_school'

            education_info['education_details'] = degrees_found

        return education_info

    def _extract_experience(self, text: str) -> Dict:
        """
        Trích xuất thông tin kinh nghiệm
        """
        experience_info = {
            'total_years': 0,
            'companies': [],
            'positions': []
        }

        # Extract years of experience
        years_matches = re.findall(self.experience_pattern, text, re.IGNORECASE)
        if years_matches:
            experience_info['total_years'] = max(int(year) for year in years_matches)

        # Common company indicators (simplified)
        company_indicators = ['at', 'worked at', 'employed at', 'company']
        text_lower = text.lower()

        # This is a simplified approach - in production, you'd use more sophisticated NLP
        sentences = text.split('.')
        for sentence in sentences:
            if any(indicator in sentence.lower() for indicator in company_indicators):
                # Extract company names (this is basic, would need NER for better accuracy)
                words = sentence.split()
                for i, word in enumerate(words):
                    if word in company_indicators and i + 1 < len(words):
                        company_name = words[i + 1].strip('.,!?')
                        if len(company_name) > 2 and company_name not in experience_info['companies']:
                            experience_info['companies'].append(company_name)

        return experience_info

    def _extract_projects(self, text: str) -> Dict:
        """
        Trích xuất thông tin dự án
        """
        project_info = {
            'projects': [],
            'project_count': 0
        }

        # Project indicators
        project_indicators = [
            'project:', 'projects:', 'developed', 'implemented', 'created',
            'designed', 'built', 'led', 'managed', 'architected'
        ]

        text_lower = text.lower()
        sentences = text.split('.')

        for sentence in sentences:
            if any(indicator in sentence.lower() for indicator in project_indicators):
                # Clean and format project description
                project_desc = sentence.strip()
                if len(project_desc) > 20:  # Filter out very short matches
                    project_info['projects'].append(project_desc)

        project_info['project_count'] = len(project_info['projects'])

        # Limit to top 5 most relevant projects
        if project_info['projects']:
            project_info['projects'] = project_info['projects'][:5]

        return project_info

    def _extract_certifications(self, text: str) -> Dict:
        """
        Trích xuất thông tin chứng chỉ
        """
        certification_info = {
            'certifications': [],
            'certification_count': 0
        }

        # Certification indicators
        cert_indicators = [
            'certified', 'certificate', 'certification', 'cisco', 'aws certified',
            'google certified', 'microsoft certified', 'pmp', 'csm', 'csd'
        ]

        text_lower = text.lower()
        sentences = text.split('.')

        for sentence in sentences:
            if any(indicator in sentence.lower() for indicator in cert_indicators):
                cert_desc = sentence.strip()
                if len(cert_desc) > 10:
                    certification_info['certifications'].append(cert_desc)

        certification_info['certification_count'] = len(certification_info['certifications'])

        return certification_info

    def _extract_languages(self, text: str) -> Dict:
        """
        Trích xuất thông tin ngoại ngữ
        """
        language_info = {
            'languages': [],
            'language_count': 0
        }

        # Common languages
        languages = [
            'english', 'vietnamese', 'chinese', 'japanese', 'korean',
            'french', 'german', 'spanish', 'russian', 'arabic'
        ]

        text_lower = text.lower()
        found_languages = []

        for lang in languages:
            if lang in text_lower:
                found_languages.append(lang.capitalize())

        language_info['languages'] = found_languages
        language_info['language_count'] = len(found_languages)

        return language_info

    def _get_empty_result(self, file_name: str) -> Dict:
        """
        Return empty result structure for failed processing
        """
        return {
            'file_name': file_name,
            'file_type': 'unknown',
            'extracted_at': datetime.now().isoformat(),
            'raw_text': '',
            'email': '',
            'phone': '',
            'name': '',
            'linkedin': '',
            'github': '',
            'skills_by_category': {
                'programming': [],
                'data_science': [],
                'devops': [],
                'design': [],
                'project_management': [],
                'other': []
            },
            'all_skills': [],
            'skills_count': 0,
            'highest_degree': None,
            'education_details': [],
            'total_years': 0,
            'companies': [],
            'positions': [],
            'projects': [],
            'project_count': 0,
            'certifications': [],
            'certification_count': 0,
            'languages': [],
            'language_count': 0
        }

    def save_processing_result(self, result: Dict) -> str:
        """
        Lưu kết quả xử lý vào file JSON

        Returns:
            str: Đường dẫn đến file kết quả
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"cv_processing_result_{timestamp}.json"
        filepath = self.upload_folder / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        logger.info(f"💾 Processing result saved: {filepath}")
        return str(filepath)

def main():
    """
    Test function for CV Processor
    """
    print("=== CV Processor Test ===")

    processor = CVProcessor()

    # Test with a sample file path
    test_file = "uploads/test_cv.pdf"

    if os.path.exists(test_file):
        print(f"🔧 Testing with: {test_file}")
        result = processor.process_cv(test_file)

        print("\n📊 Extraction Results:")
        print(f"Name: {result.get('name', 'Not found')}")
        print(f"Email: {result.get('email', 'Not found')}")
        print(f"Skills found: {result.get('skills_count', 0)}")
        print(f"Projects: {result.get('project_count', 0)}")
        print(f"Certs: {result.get('certification_count', 0)}")

        # Save result
        result_file = processor.save_processing_result(result)
        print(f"✅ Results saved to: {result_file}")
    else:
        print(f"⚠ Test file not found: {test_file}")
        print("Please place a test CV file in the uploads/ directory")

if __name__ == "__main__":
    main()