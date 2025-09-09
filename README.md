# Local MySQL Backup to Dropbox

A Python script to automatically back up **MySQL databases** and upload the backups to **Dropbox**. Ideal for automated database backups using cron jobs.

## Features

* Back up one or multiple MySQL databases.
* Automatically uploads `.sql` backup files to Dropbox according to a scheduled cron job.
* Configurable database credentials and backup paths.
* Easy setup with Python and Dropbox API.

## Requirements

* Python 3.8+
* `dropbox` Python SDK:

  ```bash
  pip install -r requirements.txt
  ```
* `mysqldump` must be installed and accessible in your system PATH.

## Setup

1. **Create a Dropbox App**

   * Go to [Dropbox App Console](https://www.dropbox.com/developers/apps)
   * Create a new app with **Full Dropbox** or **App Folder** access.
   * Add Permission [files.content.write, files.content.read] in Permissions Tab
   * Generate an **Access Token**.

2. **Configure the script**
   Open `app.py` and set your MySQL and Dropbox details in config.json file

## Scheduling Backups with Cron

Use `cron` to schedule automatic backups. You can use [crontab.guru](https://crontab.guru/) to generate cron expressions.

### Example: Run every hour

```bash
0 * * * * python /home/LocalMySQLBackup/app.py
```

* This will create backups and upload them to Dropbox every hour.

## License

This project is licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.
See [LICENSE](LICENSE) for details.

## Disclaimer

This software is provided “as-is” without any warranty.