import os
import subprocess
import time

print('Starting...')
value = subprocess.getoutput("""pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install datefinder""")


if 'not found' in value:
    os.system("""pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip3 install datefinder""")

print('SETUP COMPLETE')


