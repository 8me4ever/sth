from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pandas', 'tkinter', 'openpyxl', 'matplotlib'],
    'includes': ['PyQt5', 'PyQt5.QtQml', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets'],
    'hookspath': ['./hooks'],  # 指定自定义 hook 文件路径
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
