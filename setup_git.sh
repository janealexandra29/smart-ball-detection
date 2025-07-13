#!/bin/bash
# Smart Ball Detection - Git Setup Script

echo "🚀 Setting up Git repository for Smart Ball Detection"
echo "=================================================="

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Smart Ball Detection Flask App

Features:
- Accurate ball detection (tested on localhost:5000)
- Upload image functionality  
- Webcam capture with live preview
- Beautiful responsive UI
- Team: Alvin, Daffa, Abidzar, Ridho
- Roboflow AI integration
- Ready for deployment"

echo ""
echo "✅ Git repository initialized!"
echo ""
echo "🌐 Next steps:"
echo "1. Create new repository on GitHub.com"
echo "2. Copy the repository URL"
echo "3. Run these commands:"
echo ""
echo "git remote add origin https://github.com/USERNAME/REPO-NAME.git"
echo "git branch -M main" 
echo "git push -u origin main"
echo ""
echo "🚀 Then deploy to Render.com or Railway.app!"
