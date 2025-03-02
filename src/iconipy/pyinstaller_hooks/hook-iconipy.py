from PyInstaller.utils.hooks import collect_data_files

# Collect data files from the "assets" folder in the "iconipy" module
datas = collect_data_files('iconipy')

hiddenimports = ['tkinter', 'PIL']