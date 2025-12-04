#!/usr/bin/env python3
"""
Recommendation Engine - Enhanced HR DSS
Module phân tích gap và đưa ra gợi ý phát triển kỹ năng
"""

import json
import logging
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)

class RecommendationEngine:
    """
    Recommendation Engine - Phân tích gap và gợi ý phát triển kỹ năng
    """

    def __init__(self, skills_db_path: str = "models/skills_database.json"):
        self.skills_db_path = Path(skills_db_path)
        self.skills_database = self._load_skills_database()

        # Learning resources database
        self.learning_resources = self._build_learning_resources()

        logger.info("🎯 Recommendation Engine initialized")

    def _load_skills_database(self) -> Dict:
        """
        Load skills database hoặc tạo mới nếu chưa có
        """
        if self.skills_db_path.exists():
            try:
                with open(self.skills_db_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"⚠ Could not load skills database: {e}")

        # Create default skills database
        default_db = self._create_default_skills_database()
        self._save_skills_database(default_db)
        return default_db

    def _create_default_skills_database(self) -> Dict:
        """
        Tạo database kỹ năng mặc định
        """
        return {
            "data_science": {
                "required_skills": ["python", "sql", "statistics"],
                "advanced_skills": ["machine learning", "deep learning", "nlp"],
                "tool_skills": ["tensorflow", "pytorch", "scikit-learn", "pandas", "numpy"],
                "business_skills": ["data storytelling", "business acumen", "problem solving"],
                "career_progression": {
                    "junior": ["python", "sql", "statistics", "excel"],
                    "mid": ["python", "sql", "machine learning", "data visualization"],
                    "senior": ["python", "sql", "machine learning", "deep learning", "mlops", "leadership"],
                    "lead": ["python", "sql", "machine learning", "deep learning", "mlops", "leadership", "strategic thinking"]
                }
            },
            "web_development": {
                "required_skills": ["html", "css", "javascript"],
                "advanced_skills": ["react", "nodejs", "typescript", "graphql"],
                "tool_skills": ["webpack", "docker", "git", "ci/cd"],
                "business_skills": ["ux design", "communication", "problem solving"],
                "career_progression": {
                    "junior": ["html", "css", "javascript", "git"],
                    "mid": ["html", "css", "javascript", "react", "nodejs", "typescript"],
                    "senior": ["html", "css", "javascript", "react", "nodejs", "typescript", "architecture", "performance"],
                    "lead": ["html", "css", "javascript", "react", "nodejs", "typescript", "architecture", "leadership", "mentoring"]
                }
            },
            "devops": {
                "required_skills": ["linux", "docker", "cloud"],
                "advanced_skills": ["kubernetes", "terraform", "ansible", "ci/cd"],
                "tool_skills": ["jenkins", "gitlab", "monitoring", "security"],
                "business_skills": ["cost optimization", "scalability", "reliability"],
                "career_progression": {
                    "junior": ["linux", "docker", "git"],
                    "mid": ["linux", "docker", "kubernetes", "aws", "ci/cd"],
                    "senior": ["linux", "docker", "kubernetes", "terraform", "ansible", "security", "performance"],
                    "lead": ["linux", "docker", "kubernetes", "terraform", "ansible", "security", "architecture", "leadership"]
                }
            },
            "mobile_development": {
                "required_skills": ["mobile_development", "programming"],
                "advanced_skills": ["react native", "flutter", "swift", "kotlin"],
                "tool_skills": ["xcode", "android studio", "firebase"],
                "business_skills": ["app store optimization", "ui/ux", "testing"],
                "career_progression": {
                    "junior": ["javascript", "react native", "mobile_development"],
                    "mid": ["javascript", "react native", "flutter", "native_development"],
                    "senior": ["javascript", "react native", "flutter", "swift", "kotlin", "architecture", "performance"],
                    "lead": ["javascript", "react native", "flutter", "swift", "kotlin", "architecture", "leadership", "strategy"]
                }
            },
            "ui_ux_design": {
                "required_skills": ["design", "ui/ux"],
                "advanced_skills": ["figma", "sketch", "adobe creative suite", "prototyping"],
                "tool_skills": ["figma", "sketch", "adobe xd", "invision"],
                "business_skills": ["user research", "design thinking", "communication"],
                "career_progression": {
                    "junior": ["design", "figma", "ui/ux"],
                    "mid": ["design", "figma", "sketch", "prototyping", "user research"],
                    "senior": ["design", "figma", "sketch", "prototyping", "user research", "design systems", "leadership"],
                    "lead": ["design", "figma", "sketch", "prototyping", "user research", "design systems", "strategy", "mentoring"]
                }
            }
        }

    def _save_skills_database(self, database: Dict):
        """
        Lưu skills database
        """
        try:
            self.skills_db_path.parent.mkdir(exist_ok=True)
            with open(self.skills_db_path, 'w', encoding='utf-8') as f:
                json.dump(database, f, indent=2, ensure_ascii=False)
            logger.info("💾 Skills database saved")
        except Exception as e:
            logger.error(f"❌ Error saving skills database: {e}")

    def _build_learning_resources(self) -> Dict:
        """
        Build learning resources database
        """
        return {
            "python": {
                "courses": [
                    {"name": "Python for Everybody", "platform": "Coursera", "level": "Beginner", "duration": "4 weeks"},
                    {"name": "Complete Python Bootcamp", "platform": "Udemy", "level": "Beginner", "duration": "22 hours"},
                    {"name": "Python Programming", "platform": "edX", "level": "Intermediate", "duration": "6 weeks"}
                ],
                "books": [
                    {"title": "Python Crash Course", "author": "Eric Matthes", "difficulty": "Beginner"},
                    {"title": "Automate the Boring Stuff", "author": "Al Sweigart", "difficulty": "Beginner"},
                    {"title": "Fluent Python", "author": "Luciano Ramalho", "difficulty": "Advanced"}
                ],
                "practice": [
                    "LeetCode Python problems",
                    "HackerRank Python challenges",
                    "Codecademy Python track"
                ]
            },
            "sql": {
                "courses": [
                    {"name": "SQL for Data Science", "platform": "Coursera", "level": "Beginner", "duration": "3 weeks"},
                    {"name": "Complete SQL Bootcamp", "platform": "Udemy", "level": "Beginner", "duration": "8 hours"}
                ],
                "books": [
                    {"title": "Learning SQL", "author": "Alan Beaulieu", "difficulty": "Beginner"},
                    {"title": "SQL in 10 Minutes", "author": "Ben Forta", "difficulty": "Beginner"}
                ],
                "practice": [
                    "SQLZoo exercises",
                    "LeetCode Database problems",
                    "HackerRank SQL challenges"
                ]
            },
            "machine_learning": {
                "courses": [
                    {"name": "Machine Learning by Andrew Ng", "platform": "Coursera", "level": "Intermediate", "duration": "11 weeks"},
                    {"name": "Machine Learning A-Z", "platform": "Udemy", "level": "Beginner", "duration": "44 hours"}
                ],
                "books": [
                    {"title": "Hands-On Machine Learning", "author": "Aurélien Géron", "difficulty": "Intermediate"},
                    {"title": "Introduction to Machine Learning", "author": "Ethem Alpaydin", "difficulty": "Beginner"}
                ],
                "practice": [
                    "Kaggle competitions",
                    "UCI Machine Learning Repository",
                    "TensorFlow/PyTorch tutorials"
                ]
            },
            "docker": {
                "courses": [
                    {"name": "Docker Mastery", "platform": "Udemy", "level": "Beginner", "duration": "14 hours"},
                    {"name": "Docker for Developers", "platform": "Pluralsight", "level": "Intermediate", "duration": "5 hours"}
                ],
                "practice": [
                    "Dockerize your existing applications",
                    "Docker Hub explore",
                    "Play with Docker (online playground)"
                ]
            },
            "kubernetes": {
                "courses": [
                    {"name": "Kubernetes for Developers", "platform": "Udemy", "level": "Intermediate", "duration": "13 hours"},
                    {"name": "Certified Kubernetes Administrator", "platform": "CNCF", "level": "Advanced", "duration": "self-paced"}
                ],
                "practice": [
                    "Kubernetes Katacoda",
                    "Minikube local setup",
                    "Kubernetes official documentation tutorials"
                ]
            },
            "react": {
                "courses": [
                    {"name": "Modern React with Redux", "platform": "Udemy", "level": "Intermediate", "duration": "48 hours"},
                    {"name": "React - The Complete Guide", "platform": "Udemy", "level": "Beginner", "duration": "40 hours"}
                ],
                "practice": [
                    "React official tutorial",
                    "Build a React project from scratch",
                    "React documentation exercises"
                ]
            },
            "javascript": {
                "courses": [
                    {"name": "JavaScript: Understanding the Weird Parts", "platform": "Udemy", "level": "Intermediate", "duration": "11 hours"},
                    {"name": "JavaScript Algorithms", "platform": "freeCodeCamp", "level": "Intermediate", "duration": "self-paced"}
                ],
                "practice": [
                    "JavaScript30",
                    "Codewars JavaScript challenges",
                    "Frontend Mentor projects"
                ]
            }
        }

    def analyze_skill_gap(self, candidate_profile: Dict, target_position: str) -> Dict:
        """
        Phân tích gap kỹ năng giữa hồ sơ ứng viên và vị trí mục tiêu

        Args:
            candidate_profile (Dict): Hồ sơ ứng viên
            target_position (str): Vị trí ứng tuyển

        Returns:
            Dict: Phân tích gap và gợi ý
        """
        try:
            # Normalize position
            target_position = self._normalize_position(target_position)

            # Get position requirements
            position_requirements = self._get_position_requirements(target_position)

            if not position_requirements:
                return self._get_no_requirements_result(target_position)

            # Get candidate skills
            candidate_skills = self._extract_candidate_skills(candidate_profile)

            # Analyze gaps
            gap_analysis = self._analyze_gaps(candidate_skills, position_requirements, target_position)

            # Generate recommendations
            recommendations = self._generate_recommendations(
                candidate_skills,
                position_requirements,
                target_position,
                candidate_profile.get('years_experience', 0)
            )

            # Calculate improvement potential
            improvement_plan = self._create_improvement_plan(gap_analysis, recommendations)

            result = {
                'target_position': target_position,
                'analysis_timestamp': datetime.now().isoformat(),
                'candidate_profile': {
                    'skills_count': len(candidate_skills),
                    'experience_years': candidate_profile.get('years_experience', 0),
                    'education_level': candidate_profile.get('education_level', 'unknown')
                },
                'skill_gap_analysis': gap_analysis,
                'recommendations': recommendations,
                'improvement_plan': improvement_plan,
                'overall_score': self._calculate_improvement_score(gap_analysis)
            }

            logger.info(f"✅ Skill gap analysis completed for {target_position}")
            return result

        except Exception as e:
            logger.error(f"❌ Error in skill gap analysis: {str(e)}")
            return self._get_error_result(target_position, str(e))

    def _normalize_position(self, position: str) -> str:
        """
        Normalize position name
        """
        position = position.lower().replace(' ', '_').replace('-', '_')

        # Map common variations
        position_mapping = {
            'data_scientist': 'data_science',
            'web_developer': 'web_development',
            'frontend_developer': 'web_development',
            'backend_developer': 'web_development',
            'fullstack_developer': 'web_development',
            'devops_engineer': 'devops',
            'mobile_developer': 'mobile_development',
            'ui_designer': 'ui_ux_design',
            'ux_designer': 'ui_ux_design',
            'ui_ux_designer': 'ui_ux_design'
        }

        return position_mapping.get(position, position)

    def _get_position_requirements(self, position: str) -> Optional[Dict]:
        """
        Get requirements for a specific position
        """
        return self.skills_database.get(position)

    def _extract_candidate_skills(self, candidate_profile: Dict) -> List[str]:
        """
        Extract skills from candidate profile
        """
        skills = set()

        # From skills field
        if 'skills' in candidate_profile:
            if isinstance(candidate_profile['skills'], str):
                skill_list = [skill.strip().lower() for skill in candidate_profile['skills'].split(',')]
                skills.update(skill_list)
            elif isinstance(candidate_profile['skills'], list):
                skills.update([skill.lower() for skill in candidate_profile['skills']])

        # From all_skills (if from CV processing)
        if 'all_skills' in candidate_profile:
            skills.update([skill.lower() for skill in candidate_profile['all_skills']])

        # From skills_by_category (if from CV processing)
        if 'skills_by_category' in candidate_profile:
            for category_skills in candidate_profile['skills_by_category'].values():
                skills.update([skill.lower() for skill in category_skills])

        return list(skills)

    def _analyze_gaps(self, candidate_skills: List[str], requirements: Dict, position: str) -> Dict:
        """
        Analyze skill gaps
        """
        required_skills = [skill.lower() for skill in requirements.get('required_skills', [])]
        advanced_skills = [skill.lower() for skill in requirements.get('advanced_skills', [])]
        tool_skills = [skill.lower() for skill in requirements.get('tool_skills', [])]

        candidate_skills_lower = [skill.lower() for skill in candidate_skills]

        # Check missing required skills
        missing_required = [skill for skill in required_skills if not any(skill in cs for cs in candidate_skills_lower)]
        missing_advanced = [skill for skill in advanced_skills if not any(skill in cs for cs in candidate_skills_lower)]
        missing_tool_skills = [skill for skill in tool_skills if not any(skill in cs for cs in candidate_skills_lower)]

        # Check existing skills
        existing_required = [skill for skill in required_skills if any(skill in cs for cs in candidate_skills_lower)]
        existing_advanced = [skill for skill in advanced_skills if any(skill in cs for cs in candidate_skills_lower)]
        existing_tool_skills = [skill for skill in tool_skills if any(skill in cs for cs in candidate_skills_lower)]

        # Calculate completion percentages
        required_completion = len(existing_required) / len(required_skills) * 100 if required_skills else 100
        advanced_completion = len(existing_advanced) / len(advanced_skills) * 100 if advanced_skills else 0
        tools_completion = len(existing_tool_skills) / len(tool_skills) * 100 if tool_skills else 0

        # Determine career level based on experience
        career_level = self._determine_career_level(candidate_skills, requirements)

        return {
            'missing_required_skills': missing_required,
            'missing_advanced_skills': missing_advanced,
            'missing_tool_skills': missing_tool_skills,
            'existing_required_skills': existing_required,
            'existing_advanced_skills': existing_advanced,
            'existing_tool_skills': existing_tool_skills,
            'completion_percentages': {
                'required': round(required_completion, 1),
                'advanced': round(advanced_completion, 1),
                'tools': round(tools_completion, 1)
            },
            'critical_gaps': missing_required,  # These are most important
            'career_level': career_level
        }

    def _determine_career_level(self, candidate_skills: List[str], requirements: Dict) -> str:
        """
        Determine career level based on skills
        """
        career_progression = requirements.get('career_progression', {})

        for level, required_skills in career_progression.items():
            candidate_skills_lower = [skill.lower() for skill in candidate_skills]
            required_skills_lower = [skill.lower() for skill in required_skills]

            match_count = sum(1 for skill in required_skills_lower if any(skill in cs for cs in candidate_skills_lower))
            completion_percentage = match_count / len(required_skills_lower) * 100

            if completion_percentage >= 70:
                return level

        return 'beginner'

    def _generate_recommendations(self, candidate_skills: List[str], requirements: Dict,
                                position: str, experience_years: int) -> Dict:
        """
        Generate skill development recommendations
        """
        gap_analysis = self._analyze_gaps(candidate_skills, requirements, position)
        recommendations = {
            'immediate_priorities': [],
            'short_term_goals': [],
            'long_term_development': [],
            'learning_resources': {},
            'estimated_timeline': {},
            'skill_certifications': []
        }

        # Immediate priorities - missing required skills
        for skill in gap_analysis['missing_required_skills']:
            recommendations['immediate_priorities'].append({
                'skill': skill,
                'priority': 'critical',
                'estimated_time': self._estimate_learning_time(skill, 'required'),
                'resources': self.learning_resources.get(skill, {}).get('courses', [])
            })

        # Short-term goals - missing advanced skills
        for skill in gap_analysis['missing_advanced_skills']:
            recommendations['short_term_goals'].append({
                'skill': skill,
                'priority': 'high',
                'estimated_time': self._estimate_learning_time(skill, 'advanced'),
                'resources': self.learning_resources.get(skill, {}).get('courses', [])
            })

        # Long-term - missing tool skills
        for skill in gap_analysis['missing_tool_skills']:
            recommendations['long_term_development'].append({
                'skill': skill,
                'priority': 'medium',
                'estimated_time': self._estimate_learning_time(skill, 'tool'),
                'resources': self.learning_resources.get(skill, {}).get('courses', [])
            })

        # Add learning resources for each recommended skill
        all_missing_skills = (gap_analysis['missing_required_skills'] +
                             gap_analysis['missing_advanced_skills'] +
                             gap_analysis['missing_tool_skills'])

        for skill in all_missing_skills:
            if skill in self.learning_resources:
                recommendations['learning_resources'][skill] = self.learning_resources[skill]

        # Generate timeline
        immediate_time = sum(self._estimate_learning_time(skill, 'required')
                           for skill in gap_analysis['missing_required_skills'])
        short_term_time = sum(self._estimate_learning_time(skill, 'advanced')
                            for skill in gap_analysis['missing_advanced_skills'])
        long_term_time = sum(self._estimate_learning_time(skill, 'tool')
                           for skill in gap_analysis['missing_tool_skills'])

        recommendations['estimated_timeline'] = {
            'immediate': f"{immediate_time} weeks",
            'short_term': f"{short_term_time} months",
            'long_term': f"{long_term_time} months"
        }

        # Add certification recommendations
        recommendations['skill_certifications'] = self._get_certification_recommendations(position, gap_analysis)

        return recommendations

    def _estimate_learning_time(self, skill: str, skill_type: str) -> int:
        """
        Estimate learning time for a skill in weeks
        """
        time_estimates = {
            'required': {
                'python': 6, 'sql': 4, 'html': 2, 'css': 2, 'javascript': 6,
                'linux': 8, 'docker': 4, 'design': 6, 'programming': 8
            },
            'advanced': {
                'machine_learning': 12, 'deep_learning': 16, 'kubernetes': 8,
                'tensorflow': 10, 'pytorch': 10, 'react': 8, 'nodejs': 8
            },
            'tool': {
                'git': 2, 'aws': 10, 'azure': 10, 'terraform': 6, 'jenkins': 4,
                'figma': 4, 'sketch': 4, 'webpack': 3, 'typescript': 4
            }
        }

        base_time = time_estimates.get(skill_type, {}).get(skill, 4)

        # Adjust based on skill complexity
        if skill in ['machine_learning', 'deep_learning', 'kubernetes']:
            return max(base_time, 12)
        elif skill in ['python', 'javascript', 'react']:
            return max(base_time, 6)
        else:
            return base_time

    def _get_certification_recommendations(self, position: str, gap_analysis: Dict) -> List[Dict]:
        """
        Get certification recommendations based on position and gaps
        """
        cert_recommendations = []

        # Position-specific certifications
        position_certs = {
            'data_science': [
                {'name': 'AWS Certified Data Scientist', 'provider': 'AWS', 'level': 'Associate'},
                {'name': 'Microsoft Certified: Azure Data Scientist', 'provider': 'Microsoft', 'level': 'Associate'},
                {'name': 'Google Cloud Data Engineer', 'provider': 'Google', 'level': 'Associate'}
            ],
            'web_development': [
                {'name': 'AWS Certified Developer', 'provider': 'AWS', 'level': 'Associate'},
                {'name': 'Microsoft Certified: Azure Developer', 'provider': 'Microsoft', 'level': 'Associate'},
                {'name': 'MongoDB Certified Developer', 'provider': 'MongoDB', 'level': 'Associate'}
            ],
            'devops': [
                {'name': 'AWS Certified DevOps Engineer', 'provider': 'AWS', 'level': 'Professional'},
                {'name': 'Certified Kubernetes Administrator', 'provider': 'CNCF', 'level': 'Professional'},
                {'name': 'Docker Certified Associate', 'provider': 'Docker', 'level': 'Associate'}
            ]
        }

        if position in position_certs:
            cert_recommendations.extend(position_certs[position])

        # Skill-specific certifications
        missing_skills = gap_analysis['missing_required_skills'] + gap_analysis['missing_advanced_skills']

        skill_certs = {
            'aws': [{'name': 'AWS Cloud Practitioner', 'provider': 'AWS', 'level': 'Foundation'}],
            'docker': [{'name': 'Docker Certified Associate', 'provider': 'Docker', 'level': 'Associate'}],
            'kubernetes': [{'name': 'Certified Kubernetes Administrator', 'provider': 'CNCF', 'level': 'Professional'}],
            'python': [{'name': 'PCAP: Certified Associate in Python Programming', 'provider': 'Python Institute', 'level': 'Associate'}]
        }

        for skill in missing_skills:
            if skill.lower() in skill_certs:
                cert_recommendations.extend(skill_certs[skill.lower()])

        return cert_recommendations[:5]  # Limit to top 5 recommendations

    def _create_improvement_plan(self, gap_analysis: Dict, recommendations: Dict) -> Dict:
        """
        Create structured improvement plan
        """
        plan = {
            'phase_1': {
                'duration': '0-3 months',
                'focus': 'Critical Skill Development',
                'actions': [],
                'success_metrics': []
            },
            'phase_2': {
                'duration': '3-6 months',
                'focus': 'Advanced Skill Building',
                'actions': [],
                'success_metrics': []
            },
            'phase_3': {
                'duration': '6-12 months',
                'focus': 'Mastery and Specialization',
                'actions': [],
                'success_metrics': []
            }
        }

        # Phase 1 - Critical skills
        for priority in recommendations['immediate_priorities']:
            plan['phase_1']['actions'].append(f"Learn {priority['skill']} ({priority['estimated_time']} weeks)")
            plan['phase_1']['success_metrics'].append(f"Complete {priority['skill']} course/project")

        # Phase 2 - Advanced skills
        for goal in recommendations['short_term_goals']:
            plan['phase_2']['actions'].append(f"Master {goal['skill']} ({goal['estimated_time']})")
            plan['phase_2']['success_metrics'].append(f"Build project with {goal['skill']}")

        # Phase 3 - Long-term development
        for development in recommendations['long_term_development']:
            plan['phase_3']['actions'].append(f"Specialize in {development['skill']}")
            plan['phase_3']['success_metrics'].append(f"Get certification in {development['skill']}")

        return plan

    def _calculate_improvement_score(self, gap_analysis: Dict) -> Dict:
        """
        Calculate improvement potential score
        """
        required_completion = gap_analysis['completion_percentages']['required']
        advanced_completion = gap_analysis['completion_percentages']['advanced']
        tools_completion = gap_analysis['completion_percentages']['tools']

        # Weighted score (required skills are most important)
        overall_score = (required_completion * 0.5 +
                        advanced_completion * 0.3 +
                        tools_completion * 0.2)

        return {
            'overall_score': round(overall_score, 1),
            'readiness_level': self._get_readiness_level(overall_score),
            'improvement_potential': round(100 - overall_score, 1),
            'estimated_time_to_readiness': self._estimate_time_to_readiness(gap_analysis)
        }

    def _get_readiness_level(self, score: float) -> str:
        """
        Get readiness level based on score
        """
        if score >= 80:
            return "Highly Ready"
        elif score >= 60:
            return "Moderately Ready"
        elif score >= 40:
            return "Needs Development"
        else:
            return "Significant Development Needed"

    def _estimate_time_to_readiness(self, gap_analysis: Dict) -> str:
        """
        Estimate time to become job-ready
        """
        missing_critical = len(gap_analysis['missing_required_skills'])
        missing_advanced = len(gap_analysis['missing_advanced_skills'])

        # Average time estimates
        critical_time = missing_critical * 6  # 6 weeks per critical skill
        advanced_time = missing_advanced * 8  # 8 weeks per advanced skill

        total_weeks = critical_time + advanced_time

        if total_weeks <= 8:
            return "2 months"
        elif total_weeks <= 16:
            return "4 months"
        elif total_weeks <= 24:
            return "6 months"
        elif total_weeks <= 36:
            return "9 months"
        else:
            return "12+ months"

    def _get_no_requirements_result(self, position: str) -> Dict:
        """
        Return result when position requirements are not found
        """
        return {
            'target_position': position,
            'analysis_timestamp': datetime.now().isoformat(),
            'error': f"No requirements found for position: {position}",
            'recommendations': [],
            'improvement_plan': {}
        }

    def _get_error_result(self, position: str, error_message: str) -> Dict:
        """
        Return error result
        """
        return {
            'target_position': position,
            'analysis_timestamp': datetime.now().isoformat(),
            'error': error_message,
            'recommendations': [],
            'improvement_plan': {}
        }

    def generate_report(self, analysis_result: Dict) -> str:
        """
        Generate human-readable report
        """
        if 'error' in analysis_result:
            return f"Error: {analysis_result['error']}"

        report = []
        report.append(f"📊 SKILL GAP ANALYSIS REPORT")
        report.append(f"Position: {analysis_result['target_position'].replace('_', ' ').title()}")
        report.append(f"Generated: {analysis_result['analysis_timestamp']}")
        report.append("")

        # Gap Analysis Summary
        gap_analysis = analysis_result['skill_gap_analysis']
        report.append("🎯 SKILL GAP ANALYSIS:")
        report.append(f"Required Skills Completion: {gap_analysis['completion_percentages']['required']}%")
        report.append(f"Advanced Skills Completion: {gap_analysis['completion_percentages']['advanced']}%")
        report.append(f"Tools Skills Completion: {gap_analysis['completion_percentages']['tools']}%")
        report.append("")

        # Critical Gaps
        if gap_analysis['critical_gaps']:
            report.append("⚠️ CRITICAL SKILL GAPS (Must Learn):")
            for skill in gap_analysis['critical_gaps']:
                report.append(f"  • {skill}")
            report.append("")

        # Recommendations
        recommendations = analysis_result['recommendations']
        if recommendations['immediate_priorities']:
            report.append("🚀 IMMEDIATE PRIORITIES (Next 1-3 months):")
            for priority in recommendations['immediate_priorities']:
                report.append(f"  • {priority['skill']} - {priority['estimated_time']} weeks")
            report.append("")

        # Improvement Plan
        improvement_plan = analysis_result['improvement_plan']
        report.append("📈 IMPROVEMENT PLAN:")
        for phase, details in improvement_plan.items():
            if details['actions']:
                report.append(f"  {details['duration']}: {details['focus']}")
                for action in details['actions'][:3]:  # Limit to first 3 actions
                    report.append(f"    • {action}")

        # Overall Score
        score_info = analysis_result['overall_score']
        report.append("")
        report.append(f"📊 OVERALL READINESS: {score_info['readiness_level']}")
        report.append(f"Score: {score_info['overall_score']}/100")
        report.append(f"Estimated time to readiness: {score_info['estimated_time_to_readiness']}")

        return "\n".join(report)

def main():
    """
    Test function for Recommendation Engine
    """
    print("=== Recommendation Engine Test ===")

    engine = RecommendationEngine()

    # Test candidate profile
    test_candidate = {
        'candidate_id': 'TEST_001',
        'skills': 'python, html, css, git',
        'years_experience': 2,
        'education_level': 'bachelor',
        'projects': 'Built a personal website',
        'certifications': []
    }

    target_position = 'data_scientist'

    print(f"🎯 Analyzing skill gap for: {target_position}")
    result = engine.analyze_skill_gap(test_candidate, target_position)

    # Generate and print report
    report = engine.generate_report(result)
    print("\n" + report)

    # Save detailed result
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result_file = f"skill_gap_analysis_{timestamp}.json"

    try:
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Detailed analysis saved to: {result_file}")
    except Exception as e:
        print(f"❌ Error saving result: {e}")

if __name__ == "__main__":
    main()