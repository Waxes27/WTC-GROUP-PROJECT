import os
import sys
import subprocess

list_of_usernames = ['ndumasi','bidaniel','vpekane','sbaloyi','apillay','nwalter','cdu-pree','dchappie','fmokoena','sigamede','tmentor','tmoshole','vsithole']
list_ = ['ndumasi', 'tmentor', 'dchappie']

"""
git checkout "branch name"
git merge Playground
"""

def number_of_usernames():
    return len(list_of_usernames)


def qwer():
    for i in range(number_of_usernames()):
        for i in list_:
            os.system(f"git checkout {i}")
            os.system(f"git merge Playground")

qwer()