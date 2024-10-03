from setuptools import setup

APP = ['main.py']  # 你的主入口文件
DATA_FILES = []  # 如果有额外的资源文件，可以在这里添加
OPTIONS = {
    'argv_emulation': True,  # 允许应用程序接收命令行参数
    'packages': ['pandas', 'tkinter', 'openpyxl', 'matplotlib'],  # 需要打包的库
    'iconfile': 'icon.icns',  # 如果有自定义图标，可以添加
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
