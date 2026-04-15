# 🎓 Intelligent Certificate Verification System

An AI-powered certificate verification system that detects fraudulent academic certificates using OCR, Error Level Analysis (ELA), and database validation.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.1.3-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

- **Multi-Layer Verification**: Combines OCR, ELA, and database validation
- **95% Accuracy**: Highly accurate detection of fraudulent certificates
- **Real-time Processing**: 3-5 second verification time
- **Web Interface**: User-friendly Flask application
- **Admin Dashboard**: Comprehensive analytics and reporting
- **Export Functionality**: Download verification reports as CSV
- **Detailed Logging**: Complete audit trail of all verifications

## 🎯 Demo

### Certificate Upload Interface
Upload any certificate image for instant verification

### Verification Results
- ✅ Extracted data from certificate
- ✅ Database verification status
- ✅ Tampering detection score
- ✅ ELA visualization
- ✅ Final authenticity rating

### Admin Dashboard
- Total verifications count
- Success rate statistics
- Detailed verification logs
- CSV export functionality

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- 8GB RAM (16GB recommended)
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/certificate-verification.git
cd certificate-verification

# Install dependencies
pip install -r requirements.txt

# Initialize database
python database.py

# Run the application
python app.py
```

Visit `http://localhost:5000` in your browser.

⚠️ **Change these credentials before deployment!**

## 📁 Project Structure

```
certificate-verification/
├── app.py                    # Main Flask application
├── ocr_module.py            # OCR text extraction
├── ela_module.py            # Tampering detection
├── database.py              # Database operations
├── scoring.py               # Scoring algorithm
├── logger.py                # Logging system
├── annotation_parser.py     # Annotation handling
├── requirements.txt         # Dependencies
├── certificates.db          # SQLite database
└── dataset/
    ├── clean/              # Authentic certificates
    ├── tampered/           # Fake certificates
    ├── _annotations.txt    # Bounding boxes
    └── _classes.txt        # Field labels
```

## 🔧 How It Works

### 1. Data Extraction (OCR)
- Uses EasyOCR to extract text from predefined regions
- Processes: Student Name, Course, University, Issue Date
- Bounding boxes defined in annotation files

### 2. Tampering Detection (ELA)
- Analyzes image compression artifacts
- Detects manipulated regions
- Generates tampering score based on pixel differences

### 3. Database Validation
- Fuzzy string matching against authentic certificates
- Similarity thresholds:
  - Student Name: 80%
  - Course: 80%
  - University: 70%
  - Issue Date: 60%

### 4. Scoring Algorithm
```
Database Match:    +60 points
Database Mismatch: -40 points
No Tampering:      +40 points
Possible Tampering: +10 points
High Tampering:    -20 points
```

**Final Classification:**
- Score ≥ 80: **Highly Authentic** ✅
- Score 40-79: **Likely Authentic** ⚠️
- Score < 40: **Suspicious** ❌

## 📊 Performance Metrics

| Metric | Score |
|--------|-------|
| **Accuracy** | 95.0% |
| **Precision** | 96.6% |
| **Recall** | 93.3% |
| **F1-Score** | 94.9% |

Tested on 60 certificates (30 authentic, 30 tampered)

## 🌐 Deployment

### Quick Deploy Options

#### Render (Recommended - Free)
```bash
git push origin main
# Connect to Render dashboard
# Deploy from GitHub
```

#### Heroku
```bash
heroku create certificate-verification
git push heroku main
```

#### Railway
```bash
railway init
railway up
```

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.

## 📦 Dependencies

```
Flask==3.1.3
opencv-python==4.13.0.92
Pillow==12.1.1
numpy==2.4.2
torch==2.10.0
gunicorn
```

Full list in `requirements.txt`

## 🎓 Usage

### Verify a Certificate
1. Navigate to home page
2. Upload certificate image (JPG/PNG)
3. Wait for processing (3-5 seconds)
4. View detailed results

### Access Admin Dashboard
1. Go to `/admin`
2. Enter credentials
3. View analytics and logs
4. Export data as CSV

### Populate Database
```bash
# Add clean certificates to dataset/clean/
python populate_database.py
```

## 🔒 Security Notes

Before deploying to production:

```

2. **Generate new secret key**
```python
import secrets
app.secret_key = secrets.token_hex(16)
```

3. **Enable HTTPS** on your deployment platform

## 📈 Future Enhancements

- [ ] Automatic bounding box detection with YOLO
- [ ] Deep learning-based forgery detection
- [ ] Logo and seal verification
- [ ] Blockchain integration for certificate registry
- [ ] RESTful API for third-party integration
- [ ] Mobile application
- [ ] Multi-language support
- [ ] Batch processing capabilities

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 👥 Author

- vinayak 

## 🙏 Acknowledgments
- Flask framework
- OpenCV community
- PyTorch team

## 📞 Support

For questions or issues:
- Create a GitHub issue
- Email: A25ariu0013@bennet.edu.in
- Documentation: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

## 📚 Documentation

- [Deployment Guide](DEPLOYMENT_GUIDE.md)
- [Project Report](Certificate_Verification_Project_Report.docx)
- [API Documentation](docs/API.md) (Coming soon)

---

**Built with ❤️ for academic integrity**

⭐ Star this repo if you find it helpful!
