# HR Intelligence System v4.0 - Enhanced

🚀 **AI-Powered Recruitment System with CV Processing & Skill Recommendations**

## 🌟 Tính năng nổi bật

### 🔍 **Input đa dạng**
- **CV Processing**: Upload CV PDF/Image và tự động trích xuất thông tin bằng OCR
- **Manual Entry**: Nhập thông tin ứng viên thủ công
- **Batch Processing**: Xử lý hàng loạt từ file CSV
- **Multi-format Support**: PDF, JPG, PNG, BMP, TIFF

### 🧠 **AI-powered Analysis**
- **Machine Learning Model**: Random Forest với accuracy >85%
- **Skill-based Logic**: Kiểm tra kỹ năng bắt buộc theo vị trí
- **Experience & Education Scoring**: Đánh giá kinh nghiệm và học vấn
- **Hybrid Approach**: Kết hợp ML và rule-based logic

### 📈 **Recommendation Engine**
- **Skill Gap Analysis**: Phân tích kỹ năng còn thiếu
- **Personalized Learning Plans**: Lộ trình học tập cá nhân hóa
- **Resource Recommendations**: Courses, books, certifications
- **Timeline & Cost Estimation**: Kế hoạch chi tiết với chi phí dự kiến

### 🎯 **Position-Specific Requirements**
- **20+ Job Positions**: Data Science, Web Development, DevOps, etc.
- **Required vs Preferred Skills**: Phân loại kỹ năng bắt buộc và ưu tiên
- **Career Progression Mapping**: Lộ trình phát triển theo từng cấp bậc
- **Industry Standards**: Theo tiêu chuẩn ngành công nghệ

## 🏗️ Kiến trúc hệ thống

```
HR Intelligence System v4.0
├── 📁 Core System
│   ├── hr_dss_main.py           # Main HR Decision Support System
│   ├── cv_processor.py          # CV Processing & OCR Engine
│   └── recommendation_engine.py # Skill Gap Analysis & Recommendations
├── 🌐 Web Application
│   ├── app.py                   # Flask Web Server
│   └── templates/              # HTML Templates
├── 🤖 Machine Learning
│   ├── models/                 # Trained Models & Configurations
│   └── data/                   # Training & Sample Data
├── 📄 Enhanced Features
│   ├── uploads/                # File Upload Storage
│   ├── logs/                   # System Logs
│   └── temp/                   # Temporary Files
└── ⚙️ Setup & Configuration
    ├── requirements.txt        # Python Dependencies
    └── setup_enhanced.py       # Automated Setup Script
```

## 🚀 Quick Start

### 1. Cài đặt tự động (Recommended)

```bash
# Clone repository
git clone <repository-url>
cd HR_Linux

# Run automated setup
python setup_enhanced.py

# Start the application
python app.py
```

### 2. Cài đặt thủ công

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Tesseract OCR (for CV processing)
# Ubuntu/Debian:
sudo apt-get install tesseract-ocr tesseract-ocr-vie

# macOS:
brew install tesseract

# Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# Download spaCy model
python -m spacy download en_core_web_sm

# Run the application
python app.py
```

## 🌐 Access the System

Open your browser and navigate to: **http://localhost:5000**

### Main Features:
- **🏠 Dashboard**: http://localhost:5000
- **🧠 Train Model**: http://localhost:5000/train
- **🎯 Single Prediction**: http://localhost:5000/predict
- **📄 Upload CV**: http://localhost:5000/upload-cv *(NEW)*
- **📊 Batch Processing**: http://localhost:5000/batch
- **📈 Improvement Plan**: http://localhost:5000/improvement-plan *(NEW)*

## 📋 Các bước sử dụng

### 1. Huấn luyện mô hình
- Vào trang `/train`
- Click "Huấn luyện mô hình"
- Đợi quá trình hoàn thành (accuracy >85%)

### 2. Đánh giá ứng viên từ CV
- Vào trang `/upload-cv`
- Upload file CV (PDF/Image)
- Chọn vị trí ứng tuyển (tùy chọn)
- Xem kết quả phân tích và gợi ý

### 3. Tạo kế hoạch phát triển
- Vào trang `/improvement-plan`
- Nhập thông tin ứng viên
- Chọn vị trí mục tiêu
- Nhận lộ trình học tập chi tiết

### 4. Xử lý hàng loạt
- Vào trang `/batch`
- Upload file CSV
- Xem báo cáo tổng hợp

## 📊 Kết quả phân tích

### CV Processing Output:
```json
{
  "cv_data": {
    "file_name": "candidate_cv.pdf",
    "email": "candidate@email.com",
    "phone": "+1234567890",
    "all_skills": ["python", "sql", "machine learning"],
    "total_years": 5,
    "highest_degree": "master",
    "projects": ["Project 1", "Project 2"],
    "certifications": ["AWS Certified"]
  },
  "prediction": {
    "prediction": "Suitable",
    "confidence": 0.85,
    "recommendation": "Highly recommended for interview"
  }
}
```

### Improvement Plan Output:
```json
{
  "skill_gap_analysis": {
    "missing_required_skills": ["docker", "kubernetes"],
    "completion_percentages": {
      "required": 75,
      "advanced": 60,
      "tools": 40
    }
  },
  "next_steps": [
    {"action": "Learn Docker", "priority": "High", "estimated_time": "4 weeks"}
  ],
  "estimated_cost": {
    "total_estimated": 450,
    "courses": 200,
    "certifications": 250
  }
}
```

## 🎯 Các vị trí hỗ trợ

### Technology & Development:
- **Data Scientist**: Python, SQL, Machine Learning, Statistics
- **Web Developer**: HTML, CSS, JavaScript, React, Node.js
- **Backend Developer**: Python, Java, API, Database
- **Frontend Developer**: React, Vue, Angular, UI/UX
- **Full Stack Developer**: Combination of frontend & backend
- **Mobile Developer**: React Native, Flutter, Swift, Kotlin

### DevOps & Infrastructure:
- **DevOps Engineer**: Docker, Kubernetes, AWS, CI/CD
- **System Administrator**: Linux, Windows, Networking

### Design & Product:
- **UI/UX Designer**: Figma, Sketch, Prototyping, User Research
- **Product Manager**: Agile, User Research, Analytics, Roadmap

### Data & Analytics:
- **Data Analyst**: SQL, Excel, Power BI, Statistics
- **Business Analyst**: Requirements Analysis, Business Intelligence

## 🔧 Advanced Configuration

### Custom Position Requirements:
```python
# Edit models/position_requirements_enhanced.json
{
  "custom_position": {
    "min_years": 3,
    "min_education": "bachelor"
  }
}
```

### Custom Skill Categories:
```python
# Edit cv_processor.py to add new skill categories
self.new_category_skills = [
    'skill1', 'skill2', 'skill3'
]
```

### Model Retraining:
```python
# Retrain with custom data
from hr_dss_main import HRDecisionSupportSystemEnhanced
hr_system = HRDecisionSupportSystemEnhanced()
accuracy = hr_system.train_model(custom_data_df)
```

## 📝 API Endpoints

### System Status:
```http
GET /api/status
```

### Sample Data:
```http
GET /api/sample-data
```

### Batch Processing (via POST):
```http
POST /batch
Content-Type: multipart/form-data
```

## 🐛 Troubleshooting

### Common Issues:

1. **CV Processing Errors**:
   - Ensure Tesseract OCR is installed
   - Check file format (PDF, JPG, PNG)
   - Verify image quality

2. **Memory Issues**:
   - Reduce batch size for large CSV files
   - Close unused applications
   - Increase system RAM if needed

3. **Model Accuracy**:
   - Retrain with more diverse data
   - Check feature extraction process
   - Validate input data quality

### Logs:
- System logs: `logs/hr_dss_enhanced.log`
- Error logs: Check console output
- Processing logs: `uploads/` directory

## 📚 Documentation

- [CV Processing Guide](docs/CV_PROCESSING.md)
- [Recommendation Engine Guide](docs/RECOMMENDATIONS.md)
- [API Reference](docs/API_REFERENCE.md)
- [Model Training Guide](docs/MODEL_TRAINING.md)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

- **Developer**: Student
- **Course**: Hệ hỗ trợ ra quyết định, Hệ điều hành và lập trình Linux
- **Version**: 4.0 Enhanced

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the troubleshooting section
- Review the documentation

---

**HR Intelligence System v4.0** - Transforming Recruitment with AI 🤖✨