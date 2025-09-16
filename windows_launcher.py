#!/usr/bin/env python3
"""
Windows-friendly entry point for WhisperLiveKit
This script provides a simple interface for Windows users to start the application
"""

import sys
import os
import subprocess
import webbrowser
import time
from pathlib import Path

def main():
    """Main entry point that provides a user-friendly interface"""
    
    print("=" * 60)
    print("         WhisperLiveKit - Real-time Speech-to-Text")
    print("=" * 60)
    print()
    
    # Check if we're running from PyInstaller bundle
    if getattr(sys, 'frozen', False):
        # Running from PyInstaller bundle
        application_path = Path(sys.executable).parent
    else:
        # Running from source
        application_path = Path(__file__).parent
    
    print(f"Application directory: {application_path}")
    print()
    
    # Simple configuration options
    print("Configuration Options:")
    print("1. Quick Start (default settings)")
    print("2. Custom configuration")
    print("3. Help / Show all options")
    print()
    
    choice = input("Enter your choice (1-3) [1]: ").strip()
    if not choice:
        choice = "1"
    
    if choice == "3":
        # Show help
        from whisperlivekit.basic_server import main as server_main
        sys.argv = [sys.argv[0], "--help"]
        server_main()
        return
    
    elif choice == "2":
        # Custom configuration
        print()
        print("Custom Configuration:")
        model = input("Model size (tiny/base/small/medium/large-v3) [base]: ").strip() or "base"
        language = input("Language (en/fr/de/es/auto) [auto]: ").strip() or "auto"
        port = input("Port number [8000]: ").strip() or "8000"
        
        # Validate port
        try:
            port_num = int(port)
            if not (1024 <= port_num <= 65535):
                raise ValueError("Port must be between 1024 and 65535")
        except ValueError as e:
            print(f"Invalid port: {e}")
            port = "8000"
        
        diarization = input("Enable speaker identification? (y/n) [n]: ").strip().lower()
        enable_diarization = diarization in ['y', 'yes', '1', 'true']
        
        args = ["--model", model, "--language", language, "--port", port]
        if enable_diarization:
            args.append("--diarization")
            
    else:
        # Quick start with default settings
        print("Starting with default settings...")
        args = ["--model", "base", "--language", "auto"]
    
    print()
    print("Starting WhisperLiveKit server...")
    print(f"Arguments: {' '.join(args)}")
    print()
    
    # Import and run the main server
    try:
        from whisperlivekit.basic_server import main as server_main
        
        # Set up sys.argv for the server
        sys.argv = [sys.argv[0]] + args
        
        # Start the server
        print("Server is starting...")
        print("Once started, open your browser to: http://localhost:8000")
        print()
        print("Press Ctrl+C to stop the server")
        print("=" * 60)
        
        # Try to open browser after a short delay
        def open_browser():
            time.sleep(3)  # Give server time to start
            try:
                webbrowser.open("http://localhost:8000")
            except Exception:
                pass  # Ignore if browser can't be opened
        
        import threading
        browser_thread = threading.Thread(target=open_browser, daemon=True)
        browser_thread.start()
        
        # Start the server
        server_main()
        
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    except Exception as e:
        print(f"\nError starting server: {e}")
        print("\nPlease check that:")
        print("- FFmpeg is installed and in your PATH")
        print("- No other application is using the port")
        print("- You have sufficient disk space for model downloads")
        input("\nPress Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()