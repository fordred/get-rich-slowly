get-rich-slowly
===============

Automatisch beleggen in beleggingsfondsen

## Credentials

To use this, please specify your username and password in `credentials.py` like this:

    credentials = {
        'username': 'myusername',
        'password': 'mypassword',
    }

## SystemD
Copy the files to /etc/systemd/system
$ sudo systemd-analyze verify degiro.timer
$ sudo systemd-analyze verify degiro.service
$ sudo systemctl enable degiro.timer
$ sudo systemctl enable degiro.service
$ sudo systemctl start degiro.timer
$ sudo systemctl start degiro.service
$ systemctl list-timers --all
