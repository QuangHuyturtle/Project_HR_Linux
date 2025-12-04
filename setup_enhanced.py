#!/usr/bin/env python3
"""
Enhanced Setup Script for HR DSS v4.0
Script cài đặt toàn bộ hệ thống HR DSS với CV Processing và Recommendations
"""

import os
import sys
import subprocess
import platform

def print_banner():
    """Hiển thị banner hệ thống"""
    print("=" * 80)
    print("🚀 HR INTELLIGENCE SYSTEM v4.0 - ENHANCED SETUP")
    print("=" * 80)
    print("🤖 AI-Powered Recruitment System with:")
    print("   • CV Processing (PDF/Image OCR)")
    print("   • Skill Gap Analysis")
    print("   • Personalized Learning Recommendations")
    print("   • Multi-format Input Support")
    print("=" * 80)

def check_python_version():
    """Kiểm tra phiên bản Python"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ is required!")
        print(f"   Current version: {sys.version}")
        return False

    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def install_system_dependencies():
    """Cài đặt các thư viện hệ thống"""
    system = platform.system().lower()
    print(f"\n🔧 Installing system dependencies for {system}...")

    try:
        if system == "linux":
            # For Ubuntu/Debian
            print("   Installing Tesseract OCR...")
            subprocess.run(['sudo', 'apt-get', 'update'], check=True)
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'tesseract-ocr', 'tesseract-ocr-vie'], check=True)

        elif system == "darwin":
            # For macOS
            print("   Installing Tesseract OCR...")
            subprocess.run(['brew', 'install', 'tesseract'], check=True)

        elif system == "windows":
            print("   ⚠  For Windows: Please install Tesseract OCR manually")
            print("   Download from: https://github.com/UB-Mannheim/tesseract/wiki")

        else:
            print("   ⚠  Unknown system. Please install Tesseract OCR manually")

        print("✅ System dependencies check completed")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing system dependencies: {e}")
        print("   Please install Tesseract OCR manually")
        return False

def install_python_packages():
    """Cài đặt các thư viện Python"""
    print("\n📦 Installing Python packages...")

    try:
        # Upgrade pip
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)

        # Install requirements
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)

        print("✅ Python packages installed successfully")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing Python packages: {e}")
        return False

def download_nltk_data():
    """Download dữ liệu NLTK"""
    print("\n📚 Downloading NLTK data...")

    try:
        import nltk

        # Download required NLTK data
        nltk_packages = ['punkt', 'stopwords', 'wordnet', 'averaged_perceptron_tagger']

        for package in nltk_packages:
            try:
                nltk.data.find(f'tokenizers/{package}')
                print(f"   ✅ {package} already exists")
            except LookupError:
                print(f"   📥 Downloading {package}...")
                nltk.download(package, quiet=True)

        print("✅ NLTK data setup completed")
        return True

    except Exception as e:
        print(f"❌ Error downloading NLTK data: {e}")
        return False

def setup_spacy():
    """Cài đặt spaCy model"""
    print("\n🧠 Setting up spaCy...")

    try:
        import spacy

        try:
            nlp = spacy.load("en_core_web_sm")
            print("   ✅ spaCy English model already installed")
        except OSError:
            print("   📥 Downloading spaCy English model...")
            subprocess.run([sys.executable, '-m', 'spacy', 'download', 'en_core_web_sm'], check=True)

        print("✅ spaCy setup completed")
        return True

    except Exception as e:
        print(f"❌ Error setting up spaCy: {e}")
        return False

def create_directories():
    """Tạo các thư mục cần thiết"""
    print("\n📁 Creating directories...")

    directories = [
        'data',
        'models',
        'uploads',
        'logs',
        'temp',
        'static/css',
        'static/js',
        'templates'
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"   ✅ {directory}/")

    print("✅ Directories created successfully")
    return True

def initialize_models():
    """Khởi tạo các models mặc định"""
    print("\n🤖 Initializing HR models...")

    try:
        from hr_dss_main import HRDecisionSupportSystemEnhanced

        # Initialize system (this will create default models if not exist)
        hr_system = HRDecisionSupportSystemEnhanced()

        print("   ✅ HR DSS Enhanced system initialized")
        print("   ✅ Skills database created")
        print("   ✅ Position requirements loaded")

        return True

    except Exception as e:
        print(f"❌ Error initializing models: {e}")
        return False

def create_sample_files():
    """Tạo các file mẫu"""
    print("\n📄 Creating sample files...")

    try:
        # Create sample CV data
        from create_sample_data import main as create_data
        create_data()

        print("   ✅ Sample training data created")
        return True

    except Exception as e:
        print(f"❌ Error creating sample files: {e}")
        return False

def test_system():
    """Test hệ thống"""
    print("\n🧪 Testing system components...")

    tests_passed = 0
    total_tests = 5

    # Test 1: Import modules
    try:
        import cv_processor
        import recommendation_engine
        import hr_dss_main
        print("   ✅ Module imports successful")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Module import failed: {e}")

    # Test 2: CV Processor
    try:
        from cv_processor import CVProcessor
        processor = CVProcessor()
        print("   ✅ CV Processor initialized")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ CV Processor failed: {e}")

    # Test 3: Recommendation Engine
    try:
        from recommendation_engine import RecommendationEngine
        engine = RecommendationEngine()
        print("   ✅ Recommendation Engine initialized")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Recommendation Engine failed: {e}")

    # Test 4: HR System
    try:
        from hr_dss_main import HRDecisionSupportSystemEnhanced
        hr_system = HRDecisionSupportSystemEnhanced()
        print("   ✅ HR DSS System initialized")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ HR DSS System failed: {e}")

    # Test 5: Flask App
    try:
        from app import app
        print("   ✅ Flask app created successfully")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Flask app failed: {e}")

    print(f"\n🎯 Tests passed: {tests_passed}/{total_tests}")
    return tests_passed == total_tests

def print_success_message():
    """Hiển thị thông báo thành công"""
    print("\n" + "=" * 80)
    print("🎉 SETUP COMPLETED SUCCESSFULLY!")
    print("=" * 80)
    print("\n📋 Next Steps:")
    print("1. Run the web application:")
    print("   python app.py")
    print("\n2. Open browser to:")
    print("   http://localhost:5000")
    print("\n3. Try the new features:")
    print("   • Upload CV (PDF/Image): http://localhost:5000/upload-cv")
    print("   • Improvement Plan: http://localhost:5000/improvement-plan")
    print("   • Batch Processing: http://localhost:5000/batch")
    print("\n✨ Features Available:")
    print("   • AI-powered candidate screening")
    print("   • CV text extraction (OCR)")
    print("   • Skill gap analysis")
    print("   • Personalized learning recommendations")
    print("   • Multi-format input support")
    print("   • Vietnamese interface")
    print("\n💡 Tips:")
    print("   • For best OCR results, use high-quality PDFs or images")
    print("   • The system works with both English and Vietnamese CVs")
    print("   • Check the logs/ directory for detailed processing logs")
    print("\n" + "=" * 80)

def main():
    """Main setup function"""
    print_banner()

    # Check Python version
    if not check_python_version():
        return False

    # Ask user if they want to install system dependencies
    install_deps = input("\n🔧 Install system dependencies (Tesseract OCR)? [y/N]: ").lower()
    if install_deps in ['y', 'yes']:
        install_system_dependencies()
    else:
        print("⚠  Skipping system dependencies. Please install Tesseract OCR manually.")

    # Create directories
    if not create_directories():
        return False

    # Install Python packages
    if not install_python_packages():
        return False

    # Download NLTK data
    if not download_nltk_data():
        return False

    # Setup spaCy
    if not setup_spacy():
        return False

    # Initialize models
    if not initialize_models():
        return False

    # Create sample files
    if not create_sample_files():
        return False

    # Test system
    if test_system():
        print_success_message()
        return True
    else:
        print("\n❌ Some tests failed. Please check the error messages above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)