from PyInstaller.utils.hooks import collect_submodules

# 显式包含 PyQt5 模块及其子模块
hiddenimports = collect_submodules('PyQt5')
