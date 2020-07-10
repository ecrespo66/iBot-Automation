from setuptools import setup
from setuptools import find_packages
from glob import glob


setup(
    name='iBot',
    packages=['iBot Automation Library'],  # Mismo nombre que en la estructura de carpetas de arriba
    version='0.1',
    license='LGPL v3',  # La licencia que tenga tu paquete
    descriptionl='Python RPA library',
    author='Enrique Crespo',
    author_email='oname.dohe@gmail.com',
    include_package_data = True,
    data_files=[],
    install_requires=['beautifulsoup4==4.9.1','bs4==0.0.1','certifi==2020.6.20','DateTime==4.3','docx==0.2.4','docx2pdf==0.1.7',
                      'imap-tools==0.16.1','openpyxl==3.0.4','Pillow==7.1.2','PyPDF2==1.26.0','pytesseract==0.3.4','python-docx==0.8.10','selenium==3.141.0','urllib3==1.25.9'],
    url='https://github.com/ecrespo66/ibot',  # Usa la URL del repositorio de GitHub
    download_url='https://github.com/ecrespo66/iBot-Automation.git/dist/v0.1.tar.gz',  # Te lo explico a continuación
    keywords='Python RPA, Bot, Automation ',  # Palabras que definan tu paquete
    classifiers=['Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'])