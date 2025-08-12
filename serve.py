#!/usr/bin/env python3
"""
Simple HTTP server to test the Philip Wright website locally.
Run with: python3 serve.py
Then visit: http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 Philip Wright website is now running!")
        print(f"🌐 Open your browser and visit: http://localhost:{PORT}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"⏹️  Press Ctrl+C to stop the server")
        
        try:
            # Try to open the browser automatically
            webbrowser.open(f'http://localhost:{PORT}')
        except:
            pass
            
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n🛑 Server stopped.")

if __name__ == "__main__":
    main()
