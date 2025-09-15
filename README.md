# 🎨 RGB to Grayscale Converter

> A Flask-based web app to convert RGB images to grayscale using OpenCV.

![App Screenshot](https://via.placeholder.com/800x300.png?text=RGB+to+Grayscale+Converter)

---

## 📌 Features

- Upload RGB images via browser
- Convert them to grayscale using OpenCV
- Preview both original and grayscale images
- Simple, clean HTML/CSS UI
- Python Flask backend
- UID-based file naming
- CI support with GitHub Actions

---

## 🚀 Live Demo

⚠️ *This is a backend (Flask) application and cannot be deployed directly to GitHub Pages. You can deploy it to platforms like:*

- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [Fly.io](https://fly.io/)
- [Heroku](https://heroku.com)

---

## 📁 Project Structure
RGB-to-GRAYSCALE-Converter/
├── app.py # Flask backend
├── requirements.txt # Python dependencies
├── uploads/ # Stores user-uploaded & processed images
├── assets/
│ └── css/
│ └── style.css # Styling
├── public/
│ └── index.html # UI frontend
├── .github/
│ └── workflows/
│ └── python-app.yml # GitHub Actions workflow
└── uploads/
└── test_main.py # Basic test file

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/RGB-to-GRAYSCALE-Converter.git
cd RGB-to-GRAYSCALE-Converter

python -m venv venv
source venv/bin/activate       # Linux/macOS
# OR
venv\Scripts\activate          # Windows

pip install -r requirements.txt

python app.py

Then open: http://localhost:5000

✅ GitHub Actions (CI)

This repo uses GitHub Actions to:

Set up Python environment

Install requirements

Run app.py to check for errors (sanity check)

Run test(s)

See the workflow file: .github/workflows/python-app.yml

🧪 Running Tests

Tests are located in uploads/test_main.py.

To run tests locally:

pytest uploads/test_main.py

📦 Deployment

This app is best deployed to:

Render

Railway

Fly.io

Heroku

❗ GitHub Pages is for static sites only and will not work for Flask apps.

Need deployment help? Just ask!

📄 License

MIT License
© 2025 Entracloud
