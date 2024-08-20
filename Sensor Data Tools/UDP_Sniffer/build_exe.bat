rd /S /Q .\dist\UDP_Sniffer
rd /S /Q .\build\UDP_Sniffer
pyinstaller --icon=resources\dog-nose.ico --version-file=version.txt UDP_Sniffer.py
md .\dist\UDP_Sniffer\resources
xcopy /E resources .\dist\UDP_Sniffer\resources
xcopy .\UDP_Sniffer.yml .\dist\UDP_Sniffer
