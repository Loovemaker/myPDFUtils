import plistlib

data_files = []

option = {
    'iconfile': r'./assets/myPDFUtils/myPDFUtils.icns',
    'includes': [],
    'plist': r'./setup_options/py2app.plist'
}

with open(r'./setup_options/py2app.plist', 'rb') as file:
    model = plistlib.load(file)
    print(model)
    option['plist'] = model

setup_kwargs = {
    'app': ['__main__.py'],
    'data_files': data_files,
    'options': {'py2app': option},
    'setup_requires': ['py2app'],
}
