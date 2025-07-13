#!/usr/bin/env python3
"""
Auto-deployment script for Render.com
Smart Ball Detection Flask App
"""

import os
import subprocess
import sys

def run_command(cmd):
    """Run shell command and return result"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def main():
    print("🚀 Smart Ball Detection - Render.com Deployment")
    print("=" * 50)
    
    # Check if git is initialized
    if not os.path.exists('.git'):
        print("📁 Initializing Git repository...")
        success, out, err = run_command("git init")
        if not success:
            print(f"❌ Git init failed: {err}")
            return
    
    # Create .gitignore
    gitignore_content = """
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
pip-log.txt
pip-delete-this-directory.txt
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.git
.mypy_cache
.pytest_cache
.hypothesis
uploads/*.jpg
uploads/*.png
uploads/*.jpeg
uploads/*.gif
uploads/*.webp
!uploads/.gitkeep
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content.strip())
    
    # Create uploads/.gitkeep
    os.makedirs('uploads', exist_ok=True)
    with open('uploads/.gitkeep', 'w') as f:
        f.write('')
    
    # Add files to git
    print("📝 Adding files to Git...")
    run_command("git add .")
    run_command('git commit -m "Initial commit - Smart Ball Detection Flask App"')
    
    print("\n✅ Deployment files ready!")
    print("\n🌐 Next steps for Render.com deployment:")
    print("1. Go to https://render.com")
    print("2. Connect your GitHub account")
    print("3. Push this folder to a GitHub repository:")
    print("   git remote add origin https://github.com/yourusername/smart-ball-detection.git")
    print("   git branch -M main")
    print("   git push -u origin main")
    print("4. Create 'New Web Service' on Render")
    print("5. Connect your GitHub repository")
    print("6. Use these settings:")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: gunicorn app:app")
    print("   - Environment: Python 3")
    print("7. Deploy!")
    print("\n🎯 Your app will be live at: https://your-app-name.onrender.com")

if __name__ == "__main__":
    main()
