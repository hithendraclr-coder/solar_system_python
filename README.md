# 3D Solar System 🌌

An interactive 3D Solar System simulation built with Python and VPython.

## Features

- The Sun and all eight planets
- Animated planetary orbits
- Planetary rotation
- Saturn's rings
- Earth's Moon orbit
- Star-filled space background
- Mouse-controlled 3D camera

## Requirements

- Python 3.9 or newer
- VPython

## Installation

Open a terminal in this project folder and run:

```bash
python -m pip install --upgrade pip setuptools
python -m pip install vpython
```

If VPython reports a missing `pkg_resources` module, install a compatible setuptools version:

```bash
python -m pip install setuptools==80.9.0
```

## Run the project

```bash
python 3d_solar_system.py
```

The 3D simulation should open in your web browser.

## Controls

- **Rotate:** Drag with the left mouse button.
- **Zoom:** Use the mouse wheel.
- **Pan:** Right-click and drag.

## GitHub upload

1. Extract this ZIP file.
2. Open GitHub and create a new repository named `3D-Solar-System`.
3. Choose **Add file → Upload files**.
4. Upload the files inside the `3D-Solar-System` folder.
5. Commit the changes.

## Project structure

```text
3D-Solar-System/
├── 3d_solar_system.py
├── README.md
└── requirements.txt
```

## Note

This is an educational visualization. Planet sizes, distances, and orbital speeds are simplified and are not to scale.
