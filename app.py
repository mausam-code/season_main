from flask import Flask, render_template, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Project data - in a real app, this would come from a database
PROJECTS = [
    {
        "id": 1,
        "title": "Seasonal AgroFarm",
        "status": "Ongoing",
        "description": "Smart agriculture platform to monitor crops, analyze weather data, and predict yields using AI. Helps Nepali farmers make data-driven decisions and improve productivity.",
        "technologies": ["Python", "Django", "React", "TensorFlow", "PostgreSQL"],
        "github_url": "https://github.com/mausam-code/Agro-Farm",
        "demo_url": "https://seasonalagrofarm.com.np",
        "delay": 100
    },
    {
        "id": 2,
        "title": "MCQ Exam & Analytics Platform",
        "status": "Beta",
        "description": "Web-based exam practice system with live quizzes, score tracking, difficulty analytics, and AI-driven performance predictions for PSC, Loksewa, and civil service exams.",
        "technologies": ["Django", "React", "SQLite", "scikit-learn", "Bootstrap"],
        "github_url": "https://github.com/mausam-code/exam",
        "demo_url": "https://exams.season.name.np",
        "delay": 200
    },
    {
        "id": 3,
        "title": "Foreign Employment Management System",
        "status": "Ongoing",
        "description": "Manages worker profiles, OCR-based document uploads, employer–employee matching, and AI risk scoring to streamline foreign employment workflows.",
        "technologies": ["Django", "React", "TensorFlow", "PostgreSQL", "JWT"],
        "github_url": "https://github.com/mausam-code/fems",
        "demo_url": "https://fems.season.name.np",
        "delay": 300
    },
    {
        "id": 4,
        "title": "Mario Game",
        "status": "Beta",
        "description": "Classic Mario browser game built with pure HTML, CSS, and JavaScript — a fun way to master basic frontend development.",
        "technologies": ["HTML", "CSS", "JavaScript"],
        "github_url": "https://github.com/mausam-code/Mini_Mario",
        "demo_url": "https://game.season.name.np",
        "delay": 400
    },
    {
        "id": 5,
        "title": "AI PDF Tools Suite",
        "status": "Ongoing",
        "description": "All-in-one toolkit to compress, merge, split, scan, translate, and edit PDFs. Includes OCR-based text extraction, Nepali ↔ English translation, AI summarization, and watermark/signature tools.",
        "technologies": ["Python", "PyPDF2", "Transformers", "React", "Django"],
        "github_url": "https://github.com/mausam-code/pdf-tools",
        "demo_url": "https://tools.season.name.np",
        "delay": 500
    },
    {
        "id": 6,
        "title": "Nepali OCR & Document Automation",
        "status": "Planning",
        "description": "Scan, extract, and edit Nepali printed and handwritten documents. Auto-fill official forms, classify document types, and export clean PDFs for businesses and government use.",
        "technologies": ["Python", "EasyOCR", "TensorFlow", "React", "Django"],
        "github_url": "https://github.com/mausam-code/nepali-ocr-docs",
        "demo_url": "https://forms.season.name.np",
        "delay": 600
    },
    {
        "id": 7,
        "title": "Selenium Automation",
        "status": "Planning",
        "description": "Automation scripts to fill forms, scrape websites, and automate repetitive browser tasks — especially useful for government or official document submission.",
        "technologies": ["Python", "Selenium", "BeautifulSoup"],
        "github_url": "https://github.com/mausam-code/selenium-automation",
        "demo_url": "https://automation.season.name.np",
        "delay": 700
    }
]


@app.route('/')
def home():
    """Main portfolio page"""
    return render_template('index.html', projects=PROJECTS)

@app.route('/api/projects')
def get_projects():
    """API endpoint to get all projects"""
    return jsonify(PROJECTS)

@app.route('/api/projects/<int:project_id>')
def get_project(project_id):
    """API endpoint to get a specific project"""
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    if project:
        return jsonify(project)
    return jsonify({'error': 'Project not found'}), 404

@app.route('/api/time')
def get_current_time():
    """API endpoint to get current server time"""
    return jsonify({
        'timestamp': datetime.now().isoformat(),
        'formatted_time': datetime.now().strftime('%H:%M:%S'),
        'formatted_date': datetime.now().strftime('%Y-%m-%d')
    })

@app.context_processor
def utility_processor():
    """Make utility functions available in templates"""
    return dict(
        current_year=datetime.now().year,
        current_time=datetime.now().strftime('%H:%M:%S')
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)