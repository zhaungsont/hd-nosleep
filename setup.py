from setuptools import setup

APP = ["inactivity_cursor_move.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "packages": ["pyautogui", "pynput"],
    "excludes": ["rubicon"],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
