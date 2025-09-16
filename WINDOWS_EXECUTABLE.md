# Windows Executable Build Instructions

This document explains how to build and use the Windows executable version of WhisperLiveKit.

## Downloading Pre-built Executable

### From GitHub Actions

1. Go to the [Actions](https://github.com/YounGuru03/Whisper-Rec/actions) tab in this repository
2. Click on the latest "Build Windows Executable" workflow run that completed successfully
3. Scroll down to "Artifacts" and download "WhisperLiveKit-Windows"
4. Extract the ZIP file to your desired location
5. Run `start_whisperlivekit.bat` or directly run `WhisperLiveKit.exe`

### From Releases (if available)

1. Go to the [Releases](https://github.com/YounGuru03/Whisper-Rec/releases) page
2. Download the latest `WhisperLiveKit-Windows.zip` file
3. Extract it to your desired location
4. Run `start_whisperlivekit.bat` or directly run `WhisperLiveKit.exe`

## Running the Executable

### Easy Method (Recommended)
1. Double-click `start_whisperlivekit.bat`
2. Follow the on-screen prompts to configure the application
3. Your web browser will automatically open to http://localhost:8000

### Advanced Method
1. Open Command Prompt or PowerShell in the extracted folder
2. Run `WhisperLiveKit.exe --help` to see all available options
3. Run with your desired settings, for example:
   ```
   WhisperLiveKit.exe --model base --language en --port 8000
   ```

## First Time Setup

### Prerequisites
- **FFmpeg**: The executable includes most dependencies, but FFmpeg must be installed separately
  - Download from: https://ffmpeg.org/download.html
  - Add ffmpeg.exe to your Windows PATH
  - Alternative: Place ffmpeg.exe in the same folder as WhisperLiveKit.exe

### First Run
- The first time you run WhisperLiveKit, it will download AI models (can take 5-10 minutes)
- Models are downloaded to your user's cache directory and reused for subsequent runs
- Ensure you have a stable internet connection for the initial model download

## Building from Source

If you want to build the executable yourself:

### Prerequisites
- Python 3.9-3.12 (3.11 recommended)
- Git
- FFmpeg installed and in PATH

### Build Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/YounGuru03/Whisper-Rec.git
   cd Whisper-Rec
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements-build.txt
   pip install -e .
   ```

3. Create the PyInstaller spec file:
   ```bash
   python create_pyinstaller_spec.py
   ```

4. Build the executable:
   ```bash
   pyinstaller whisperlivekit.spec --clean --noconfirm
   ```

5. Find the executable in `dist/WhisperLiveKit/`

## Troubleshooting

### Common Issues

**"FFmpeg not found"**
- Ensure FFmpeg is installed and in your PATH
- Or place ffmpeg.exe in the same folder as WhisperLiveKit.exe

**"Port already in use"**
- Another application is using port 8000
- Use a different port: `WhisperLiveKit.exe --port 8001`

**"Permission denied" or antivirus warnings**
- Some antivirus software may flag the executable
- Add an exception for the WhisperLiveKit folder
- This is common with PyInstaller-built executables

**Slow first startup**
- The first run downloads AI models, which can take several minutes
- Subsequent runs will be much faster

**Application crashes on startup**
- Check that you have sufficient disk space (models can be several GB)
- Ensure no other instance is running
- Try running from Command Prompt to see error messages

### Getting Help

1. Check the console output for error messages
2. Run with `--log-level DEBUG` for more detailed logging
3. Open an issue on GitHub with:
   - Your Windows version
   - The full error message
   - Steps to reproduce the problem

## Configuration Options

The executable supports all the same configuration options as the original Python version:

- `--model`: Choose model size (tiny, base, small, medium, large-v3)
- `--language`: Set language (en, fr, de, es, auto)
- `--diarization`: Enable speaker identification
- `--port`: Change the web server port
- `--host`: Change the host address (for network access)

Run `WhisperLiveKit.exe --help` for the complete list of options.

## Web Interface

Once started, open your browser to `http://localhost:8000` to access the web interface:

1. Click "Start Recording" to begin transcription
2. Speak into your microphone
3. See real-time transcription with timestamps
4. Speaker diarization (if enabled) will identify different speakers

The web interface works with all modern browsers and requires no additional setup.