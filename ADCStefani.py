#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

TOKEN = "-JFp19x_9tYAAAAAAAAEYiQNlvI62MSjoTSKZsvUVzleK8kULo2T1-xIaWUaYhnk";

COMPRESFILE = "";
#LOCALFILE   = "D:\Python\Python.7z";
LOCALFILE   = "/home/haynes/vmware-tools-distrib.7z";
BKPFILE     = "/ADCStefani/db.backup.7z";

# Uploads contents of LOCALFILE to Dropbox
def backup():
    with open(LOCALFILE, 'r') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        print("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        try:
            dbx.files_upload(f, BACKUPPATH, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have
            # enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().error.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()

if __name__ == '__main__':
    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Looks like you didn't add your access token. Open up backup-and-restore-example.py in a text editor and paste in your token in line 14.")
    
    os.execute("7z a /home/haynes/vmware-tools-distrib "+LOCALFILE);
    
    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
    
    backup();
    
    os.execute("pause");