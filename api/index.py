#!/usr/bin/env python3
"""
Vercel WSGI Handler for Smart Ball Detection Flask App
"""

import sys
import os

# Add parent directory to path to import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel handler function
def handler(request):
    """Vercel serverless handler"""
    return app(request.environ, lambda status, headers: None)

# For Vercel
app = app

if __name__ == "__main__":
    # For local testing
    app.run(debug=True)
