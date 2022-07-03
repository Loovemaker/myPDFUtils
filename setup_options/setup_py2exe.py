option = {
    'compressed': 1,
    'optimize': 2,
    'includes': ['encodings', 'encodings.utf_8', 'lxml._elementpath'],
    'bundle_files': 1,
    'dll_excludes': ['MSVCP90.dll'],
}

window = {
    'script': r'__main__.py',  # 需要打包的程序的主文件路径
    'icon_resources': [(1, r'./assets/myPDFUtils/myPDFUtils.ico')],  # 程序的图标的图片路径
}

setup_kwargs = {
    'name': 'myPDFUtils',
    'version': '0.0.0',
    'description': "Loovemaker's PDF Utilities",
    'options': {'py2exe': option},
    'zipfile': None,
    'windows': [window],
    'setup_requires': ['py2exe', 'lxml']
}
