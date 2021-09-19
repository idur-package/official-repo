Name="tcs-cleaner"
Version="0"
Depends=["curl", "bash", "dialog", "coreutils", "sug/snapd", "sug/flatpak"]
Conflict=["tcs-cleaner"]

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="all" #all, x86_64, i386, both

Description="""
tcs-cleaner is a system cleaner script, Update your system, remove temp data,
cache files if I spend a long time without being used and remove logs.
"""

Install="""
curl https://raw.githubusercontent.com/Can202/tcs-cleaner/main/installer | bash

"""

Remove="""
tcs-cleaner-remove
"""
