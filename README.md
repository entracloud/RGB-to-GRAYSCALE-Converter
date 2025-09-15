# 🎨 RGB to Grayscale Converter

A Flask-based web app to convert RGB images to grayscale using OpenCV.

![App Screenshot](https://github.com/entracloud/RGB-to-GRAYSCALE-Converter/assets/img/working-img.png)

---

## 📌 Features

- Upload RGB images via browser
- Convert images to grayscale using OpenCV
- Preview both original and grayscale outputs
- Simple, clean HTML/CSS UI
- Python Flask backend
- UUID-based file naming
- CI support with GitHub Actions

---

## 🚀 Deployment Options

This is a backend (Flask) application and cannot be deployed to GitHub Pages (which serves static sites only). Consider:

- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [Fly.io](https://fly.io/)
- [Heroku](https://heroku.com)

---

## 📁 Project Structure

```text
RGB-to-GRAYSCALE-Converter/
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
├── uploads/                # Stores user-uploaded & processed images
├── assets/
│   └── css/
│       └── style.css       # Styling
├── public/
│   └── index.html          # UI frontend
└── .github/
   └── workflows/
       └── python-app.yml  # GitHub Actions workflow
```

Note: Paths may vary slightly based on your local changes.

---

## ⚙️ Getting Started

### 1) Clone and set up

```bash
git clone https://github.com/entracloud/RGB-to-GRAYSCALE-Converter.git
cd RGB-to-GRAYSCALE-Converter

python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

### 2) Run the app

```bash
python app.py
```

Then open your browser at:
- http://localhost:5000

If the app requires an `uploads/` directory and it doesn't exist, create it before running:
- Linux/macOS: `mkdir -p uploads`
- Windows: `mkdir uploads`

### Alternative: Flask CLI

```bash
# Linux/macOS
export FLASK_APP=app.py
export FLASK_ENV=development   # optional: enables auto-reload
flask run --port 5000

# Windows (PowerShell)
$env:FLASK_APP="app.py"
$env:FLASK_ENV="development"
flask run --port 5000
```

---

## ✅ Continuous Integration (GitHub Actions)

This repository includes a CI workflow that:
- Sets up a Python environment
- Installs requirements
- Runs a quick sanity check of the app
- Executes tests

See the workflow file:
- .github/workflows/python-app.yml

---

## 📦 Deployment Tips

- Ensure your `requirements.txt` is up to date.
- For platforms like Render/Railway/Fly.io/Heroku:
  - Set the start command to `python app.py` (or use a WSGI server like `gunicorn` if you prefer).
  - Configure any necessary environment variables (e.g., `PORT` if required by the platform).
- GitHub Pages is for static sites only and will not work for Flask apps.

Need deployment help? Open an issue or discussion in the repository.

---

## 🙌 Credits

Built with ❤️ by the [Entracloud](https://github.com/entracloud) team.

---

## 📄 License

MIT License  
© 2025 Entracloud
