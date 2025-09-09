import json
import os, sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

# Get Current Working Directory
cwd = os.getcwd()

# Config Data
config_data = []

# Read Config Json File
with open("config.json", "r") as config_file:
    config_data = json.load(config_file)

    # Credentials
    db_name = config_data['db_name']
    db_user = config_data['db_user']
    db_pass = config_data['db_pass']
    db_port = config_data['db_port']
    db_host = config_data['db_host']
    drp_token = config_data['drp_token']
    db_backup_name = config_data['db_backup_name']

# Take Database Backup
backup_path = os.path.join(cwd, db_backup_name + ".sql")
os.system("mysqldump -u " + db_user + " -p" + db_pass + " " + db_name + " > " + db_backup_name)

# Add OAuth2 access token here.
# You can generate one for yourself in the App Console.
# See <https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/>
TOKEN = drp_token
LOCALFILE = backup_path
BACKUPPATH = '/Backup/' + db_backup_name + '.sql'

# Upload Database Backup
dbx = dropbox.Dropbox(TOKEN)

# Uploads contents of LOCALFILE to Dropbox
def backup_db():
    with open(LOCALFILE, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        print("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        try:
            dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have
            # enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()


# Backup Local TXT File
backup_db()
