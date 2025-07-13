#!/usr/bin/env python3
"""
Auto-deployment script for Railway.app
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
    print("🚂 Smart Ball Detection - Railway.app Deployment")
    print("=" * 50)
    
    # Check if Railway CLI is installed
    success, out, err = run_command("railway --version")
    if not success:
        print("❌ Railway CLI not found!")
        print("📥 Install Railway CLI:")
        print("npm install -g @railway/cli")
        print("or")
        print("curl -fsSL https://railway.app/install.sh | sh")
        return
    
    print(f"✅ Railway CLI found: {out.strip()}")
    
    # Login to Railway
    print("\n🔐 Logging in to Railway...")
    print("Please run: railway login")
    print("Then run this script again.")
    
    # Check if logged in
    success, out, err = run_command("railway whoami")
    if not success:
        print("❌ Please login first: railway login")
        return
    
    print(f"✅ Logged in as: {out.strip()}")
    
    # Initialize Railway project
    print("\n🚀 Initializing Railway project...")
    success, out, err = run_command("railway init")
    if success:
        print("✅ Railway project initialized!")
    else:
        print(f"⚠️ Railway init: {err}")
    
    # Deploy
    print("\n🚀 Deploying to Railway...")
    success, out, err = run_command("railway up")
    if success:
        print("✅ Deployment successful!")
        print(f"📝 Output: {out}")
    else:
        print(f"❌ Deployment failed: {err}")
        return
    
    # Get domain
    success, out, err = run_command("railway domain")
    if success:
        print(f"\n🌐 Your app is live at: {out.strip()}")
    else:
        print("\n🌐 Check your Railway dashboard for the live URL")
    
    print("\n✅ Deployment complete!")
    print("🎯 Your Smart Ball Detection app is now live!")

if __name__ == "__main__":
    main()
