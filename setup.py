from setuptools import setup

APP = ['main.py']  # 你的主入口文件
DATA_FILES = []  # 如果有额外的资源文件，可以在这里添加
OPTIONS = {
    'argv_emulation': True,  # 启用命令行参数模拟
    'packages': ['pandas', 'tkinter', 'openpyxl', 'matplotlib'],
    'includes': ['PyInstaller.hooks.hook-gi.repository.GstWebRTC'],  # 显式包含缺失的模块
    # 'iconfile': 'icon.icns',  # 如果没有 icns 文件，可以注释掉该行
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
