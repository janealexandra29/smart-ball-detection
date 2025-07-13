#!/usr/bin/env python3
"""
Auto GitHub Upload Script
Smart Ball Detection Flask App
"""

import os
import subprocess
import sys

def run_command(cmd):
    """Run shell command"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def main():
    print("🚀 Smart Ball Detection - Auto GitHub Upload")
    print("=" * 50)
    
    # Get GitHub username
    username = input("GitHub Username: ")
    repo_name = input("Repository Name (default: smart-ball-detection): ") or "smart-ball-detection"
    
    print(f"\n📁 Creating repository: {username}/{repo_name}")
    
    # Initialize git
    print("📝 Initializing Git...")
    run_command("git init")
    run_command("git add .")
    run_command('git commit -m "Smart Ball Detection Flask App - Ready for deployment"')
    
    # Add remote
    repo_url = f"https://github.com/{username}/{repo_name}.git"
    print(f"🔗 Adding remote: {repo_url}")
    run_command(f"git remote add origin {repo_url}")
    run_command("git branch -M main")
    
    print("\n🚀 Ready to push!")
    print("Run this command to upload:")
    print(f"git push -u origin main")
    print("\nGitHub will ask for your username and token.")
    print("\n✅ After upload, deploy to:")
    print("🟢 Render.com: https://render.com")
    print("🟣 Railway.app: https://railway.app")

if __name__ == "__main__":
    main()
