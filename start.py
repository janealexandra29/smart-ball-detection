#!/usr/bin/env python3
"""
Simple start script for Railway deployment
"""

import os
from app import app

if __name__ == '__main__':
    # Railway automatically sets PORT environment variable
    port = int(os.environ.get('PORT', 5000))

    print(f"🚀 Starting on port: {port}")
    print(f"🌐 PORT env: {os.environ.get('PORT', 'Not set')}")

    # Start Flask app
    app.run(
        debug=False,
        host='0.0.0.0',
        port=port
    )
