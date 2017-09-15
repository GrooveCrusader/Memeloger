import sys
import os
import time
import codecs
import gc

import fogbugz
from fogbugz import FogBugz

import httplib2

import apiclient
from apiclient import discovery
from oauth2client import tools
from oauth2client import client
from oauth2client.file import Storage

from bs4 import BeautifulSoup

import weeklog_utility as wutil
import weeklog_requests as wrequests


try:
    import argparse
    FLAGS = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    FLAGS = None

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
DISCOVERY_URL = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'FogBugz auto weeklog'


LOG_FILE = 'log.txt'

def get_credentials():
    """
    Gets valid user credentials from storage.\n
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.\n
    Returns: Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-fogbugz-auto-weeklog.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if FLAGS:
            credentials = tools.run_flow(flow, store, FLAGS)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run_flow(flow, store)
        llog('Storing credentials to: ' + credential_path)
    else:
        llog('Loading credentials from: ' + credential_path)
    return credentials


def llog(text: str, to_console=True): # Connection loss proof
    '''
    Logs the string provided to the file
    Logs the string provided to the console if toConsole is True
    '''
    time_str = str(wutil.get_current_time())
    with codecs.open(LOG_FILE, 'a', encoding='utf-8') as file:
        file.write(time_str + ': ' + text + '\n')
    if to_console:
        print(time_str + ': ' + text)

def main():
    get_credentials()
    print("sex")


if __name__ == '__main__':
    main()