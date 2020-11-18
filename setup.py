import os
import subprocess
import time

zsh = open(f"{os.environ['HOME']}/.zshrc", 'a+')
bashrc = open(f"{os.environ['HOME']}/.bashrc", 'a+')
bashrc1 = open(f"{os.environ['HOME']}/.bashrc", 'r')

print('Starting... Do not interrupt process')
value = subprocess.getoutput("""pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install datefinder
mkdir ~/WTC-GROUP-PROJECT
git clone https://github.com/Waxes27/WTC-GROUP-PROJECT.git WTC-GROUP-PROJECT""")


if 'not found' in value:
    os.system("""pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip3 install datefinder
cp -r WTC-GROUP-PROJECT ~/Music
rm -rf WTC-GROUP-PROJECT
git clone https://github.com/Waxes27/WTC-GROUP-PROJECT.git WTC-GROUP-PROJECT""")
    
if "alias clinic" not in bashrc1.read():
    bashrc.write("\nalias clinic='python3 ~/WTC-GROUP-PROJECT/main/main.py'\n")
    zsh.write("\nalias clinic='python3 ~/WTC-GROUP-PROJECT/main/main.py'\n")



os.system("""mkdir ~/.config/.clinic

cp ~/WTC-GROUP-PROJECT/main/code/codebase/credentials.json ~/.config/.clinic
cp -r ~/WTC-GROUP-PROJECT/main/.tokens/ ~/.config/.clinic""")

# os.system("clear")
print('SETUP COMPLETE')


