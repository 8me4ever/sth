from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,  # 启用命令行参数模拟
    'packages': ['pandas', 'tkinter', 'openpyxl', 'matplotlib'],
    'includes': [
        'PyQt5', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'PyQt5.QtQml',
        'PyInstaller.hooks.hook-PyQt5.QtQml',  # 显式指定导入问题的模块
    ],
    'excludes': ['PyInstaller.hooks.hook-PyQt5.QtQml'],  # 如果无法导入，可以尝试排除
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
