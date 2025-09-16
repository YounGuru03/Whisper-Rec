#!/usr/bin/env python3
"""
Creates a PyInstaller spec file for WhisperLiveKit
"""

import os
import sys
from pathlib import Path

def create_spec_file():
    """Create the PyInstaller spec file for WhisperLiveKit"""
    
    # Get the absolute paths
    project_root = Path(__file__).parent.absolute()
    whisperlivekit_path = project_root / 'whisperlivekit'
    
    spec_content = f'''# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, r'{project_root}')

a = Analysis(
    ['windows_launcher.py'],
    pathex=[r'{project_root}'],
    binaries=[],
    datas=[
        (r'{whisperlivekit_path}/web', 'whisperlivekit/web'),
        (r'{whisperlivekit_path}/simul_whisper/whisper/assets', 'whisperlivekit/simul_whisper/whisper/assets'),
    ],
    hiddenimports=[
        'whisperlivekit',
        'whisperlivekit.basic_server',
        'whisperlivekit.audio_processor',
        'whisperlivekit.core',
        'whisperlivekit.parse_args',
        'whisperlivekit.web.web_interface',
        'whisperlivekit.simul_whisper',
        'whisperlivekit.simul_whisper.simul_whisper',
        'whisperlivekit.diarization',
        'whisperlivekit.translation',
        'fastapi',
        'uvicorn',
        'uvicorn.workers',
        'uvicorn.workers.uvicorn',
        'websockets',
        'websockets.legacy',
        'websockets.legacy.server',
        'starlette',
        'starlette.middleware',
        'starlette.middleware.cors',
        'starlette.staticfiles',
        'librosa',
        'soundfile',
        'torch',
        'torchaudio',
        'faster_whisper',
        'tiktoken',
        'numpy',
        'scipy',
        'sklearn',
        'sklearn.utils._cython_blas',
        'sklearn.neighbors.typedefs',
        'sklearn.neighbors.quad_tree',
        'sklearn.tree',
        'sklearn.tree._utils',
        'triton',
        'numba',
        'llvmlite',
        'av',
        'ctranslate2',
        'huggingface_hub',
        'tokenizers',
        'tqdm',
        'regex',
        'cffi',
        'pydantic',
        'annotated_types',
        'typing_extensions',
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'IPython',
        'jupyter',
        'notebook',
        'pandas',
        'pytest',
        'sphinx',
        'PIL.ImageTk',
        'tkinter',
    ],
    noarchive=False,
    optimize=0,
)

# Filter out some problematic binaries and libraries
a.binaries = TOC([x for x in a.binaries if not any(exclude in x[0].lower() for exclude in [
    'api-ms-win',
    'msvcp',
    'vcruntime',
    'ucrtbase'
])])

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='WhisperLiveKit',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='WhisperLiveKit',
)
'''
    
    # Write the spec file
    spec_path = project_root / 'whisperlivekit.spec'
    with open(spec_path, 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print(f"Created PyInstaller spec file: {spec_path}")
    return spec_path

if __name__ == '__main__':
    create_spec_file()