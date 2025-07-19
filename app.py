from flask import Flask, render_template, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Project data - in a real app, this would come from a database
PROJECTS = [
    {
        "id": 1,
        "title": "AI Analytics Hub",
        "status": "ongoing",
        "description": "Revolutionary AI-powered analytics platform that processes real-time data streams and provides intelligent insights for business decision making. Features advanced machine learning models and intuitive dashboards.",
        "technologies": ["React", "Python", "TensorFlow", "Node.js", "MongoDB"],
        "github_url": "https://github.com/seasonrajak/ai-analytics",
        "demo_url": "https://example.com/ai-analytics-demo",
        "delay": 100
    },
    {
        "id": 2,
        "title": "Supply Chain DApp",
        "status": "beta",
        "description": "Decentralized application for transparent supply chain management using blockchain technology. Tracks products from origin to consumer with immutable records and smart contracts.",
        "technologies": ["Solidity", "Web3.js", "Ethereum", "React", "IPFS"],
        "github_url": "https://github.com/seasonrajak/supply-chain-dapp",
        "demo_url": "https://example.com/supply-chain-demo",
        "delay": 200
    },
    {
        "id": 3,
        "title": "VR Shopping Mall",
        "status": "ongoing",
        "description": "Immersive virtual reality shopping experience that allows customers to browse and purchase products in a 3D virtual environment. Features haptic feedback and social shopping capabilities.",
        "technologies": ["Unity", "C#", "WebXR", "Three.js", "AR.js"],
        "github_url": "https://github.com/seasonrajak/vr-shopping",
        "demo_url": "https://example.com/vr-shopping-demo",
        "delay": 300
    },
    {
        "id": 4,
        "title": "Smart City IoT",
        "status": "planning",
        "description": "Comprehensive IoT platform for smart city management, integrating sensors for traffic monitoring, environmental data collection, and intelligent resource management across urban infrastructure.",
        "technologies": ["Arduino", "Raspberry Pi", "AWS IoT", "LoRaWAN", "Docker"],
        "github_url": "https://github.com/seasonrajak/smart-city-iot",
        "demo_url": "https://example.com/smart-city-demo",
        "delay": 400
    },
    {
        "id": 5,
        "title": "Quantum Simulator",
        "status": "ongoing",
        "description": "Advanced quantum computing simulator that allows researchers and developers to test quantum algorithms without access to actual quantum hardware. Features visual quantum circuit designer.",
        "technologies": ["Qiskit", "Python", "NumPy", "Matplotlib", "Jupyter"],
        "github_url": "https://github.com/seasonrajak/quantum-simulator",
        "demo_url": "https://example.com/quantum-simulator-demo",
        "delay": 500
    },
    {
        "id": 6,
        "title": "Neural Net Visualizer",
        "status": "beta",
        "description": "Interactive 3D visualization tool for neural networks that helps students and researchers understand deep learning architectures through immersive visual representations and real-time training visualization.",
        "technologies": ["D3.js", "Three.js", "TensorFlow.js", "WebGL", "React"],
        "github_url": "https://github.com/seasonrajak/neural-visualizer",
        "demo_url": "https://example.com/neural-visualizer-demo",
        "delay": 600
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