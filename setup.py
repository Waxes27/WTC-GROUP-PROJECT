import os
import subprocess
import time

bashrc = open(f"{os.environ['HOME']}/.bashrc", 'r+')

print('Starting... Do not interrupt process')
value = subprocess.getoutput("""pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install datefinder
mkdir ~/WTC-GROUP-PROJECT
git clone https://github.com/Waxes27/WTC-GROUP-PROJECT.git ~/""")


if 'not found' in value:
    os.system("""pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip3 install datefinder""")

bashrc.write("alias clinic='python3 ~/WTC-GROUP-PROJECT/main/main.py'")
os.system("""mkdir ~/.config/.clinic

cp ~/WTC-GROUP-PROJECT/main/code/codebase/credentials.json ~/.config/.clinic
cp -r ~/WTC-GROUP-PROJECT/main/.tokens/ ~/.config/.clinic""")


print('SETUP COMPLETE')


