#!/usr/bin/env python3
"""
Start script for Smart Ball Detection Flask App
Handles different hosting environments
"""

import os
import sys
from app import app

def main():
    """Start the Flask application"""
    # Get port from environment or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Determine if we're in production
    debug = os.environ.get('FLASK_ENV') != 'production'
    
    print(f"🚀 Starting Smart Ball Detection on port {port}")
    print(f"🔧 Debug mode: {debug}")
    print(f"🌐 Environment: {os.environ.get('FLASK_ENV', 'development')}")
    
    # Start the app
    app.run(
        debug=debug,
        host='0.0.0.0',
        port=port
    )

if __name__ == '__main__':
    main()
