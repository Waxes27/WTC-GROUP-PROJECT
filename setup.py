import os
import subprocess
import time

bashrc = open(f"{os.environ['HOME']}/.bashrc", 'r+')

print('Starting...')
value = subprocess.getoutput("""pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install datefinder""")


if 'not found' in value:
    os.system("""pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip3 install datefinder""")

bashrc.write("alias clinic='python3 ~/WTC-GROUP-PROJECT/main/main.py'")


print('SETUP COMPLETE')


