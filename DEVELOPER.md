# Developer Guide

This document provides instructions for developers working on WhisperLiveKit.

## Development Setup

### Local Development
```bash
git clone https://github.com/YounGuru03/Whisper-Rec.git
cd Whisper-Rec
pip install -e .
```

### GitHub Codespaces
1. Open the repository on GitHub
2. Click "Code" → "Codespaces" → "Create codespace on main"
3. Wait for automatic setup (includes FFmpeg)

## Testing

### Run All Tests
```bash
# Test build readiness
python test_build_readiness.py

# Test integration
python test_integration.py
```

### Test Server Locally
```bash
# Start with default settings
whisperlivekit-server

# Start with custom settings
whisperlivekit-server --model base --language en --port 8000
```

## Building Windows Executable

### Automated (GitHub Actions)
The easiest way is to let GitHub Actions build the executable:
1. Push changes to main branch
2. Go to Actions tab and wait for "Build Windows Executable" to complete
3. Download the artifact

### Manual Build (Advanced)
```bash
# Install build dependencies
pip install -r requirements-build.txt

# Generate PyInstaller spec
python create_pyinstaller_spec.py

# Build executable
pyinstaller whisperlivekit.spec --clean --noconfirm

# Find executable in dist/WhisperLiveKit/
```

## Project Structure

```
WhisperLiveKit/
├── whisperlivekit/              # Main package
│   ├── basic_server.py          # Main server entry point
│   ├── audio_processor.py       # Audio processing
│   ├── core.py                  # Core transcription engine
│   └── web/                     # Web interface files
├── .github/workflows/           # CI/CD workflows
├── .devcontainer/              # Codespaces configuration
├── windows_launcher.py         # User-friendly Windows entry point
├── create_pyinstaller_spec.py  # PyInstaller spec generator
├── test_build_readiness.py     # Build validation tests
└── test_integration.py         # Integration tests
```

## Key Files for Windows Executable

- **`windows_launcher.py`**: User-friendly entry point with configuration wizard
- **`create_pyinstaller_spec.py`**: Generates PyInstaller specification
- **`whisperlivekit.spec`**: PyInstaller build configuration (auto-generated)
- **`start_whisperlivekit.bat`**: Windows batch file for easy launching
- **`.github/workflows/build-windows-exe.yml`**: Automated build pipeline

## Making Changes

### Adding New Dependencies
1. Add to `pyproject.toml` under `dependencies`
2. Also add to `requirements-build.txt` if needed for Windows build
3. Update hidden imports in `create_pyinstaller_spec.py` if necessary
4. Test with `python test_build_readiness.py`

### Modifying the Build Process
1. Update `create_pyinstaller_spec.py` for PyInstaller changes
2. Update `.github/workflows/build-windows-exe.yml` for CI changes
3. Test locally or push to trigger GitHub Actions

### Adding New Features
1. Implement in the appropriate module under `whisperlivekit/`
2. Update `windows_launcher.py` if it needs UI exposure
3. Add tests and run integration tests
4. Update documentation

## Troubleshooting

### Common Issues

**Import errors during build**
- Check `hiddenimports` in `create_pyinstaller_spec.py`
- Some modules need to be explicitly listed

**Missing data files in executable** 
- Check `datas` section in `create_pyinstaller_spec.py`
- Use relative paths from project root

**Executable won't start**
- Test with `python test_integration.py` first
- Check for missing system dependencies (like FFmpeg)
- Look at console output for specific errors

**CI build fails**
- Check GitHub Actions logs
- Verify all dependencies are available on Windows
- Make sure tests pass locally first

### Getting Help

1. Check existing GitHub Issues
2. Run tests locally to isolate problems
3. Look at GitHub Actions build logs for CI issues
4. Create detailed bug reports with steps to reproduce