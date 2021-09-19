
Name="laer"
Version="v0.2"


Maintainer="Can202"
Contact="mgoopazo@gmail.com"

Arch="all"

Depends= ["vim", "bash", "neofetch"]
Conflict= ["laer"]
Description="""

clear command, but personalized, you can made a bash script to execute, when you
clear the windows with laer. Use add-link to add a 'command' to /bin or use an
alias like: alias clear=laer.

"""

Install="""

mkdir -p /etc/laer
rm -vrf /tmp/laer
mkdir -p /tmp/laer
cd /tmp/laer
curl -OL https://raw.githubusercontent.com/Can202/laer/v0.2/laer
curl -OL https://raw.githubusercontent.com/Can202/laer/v0.2/bashinstaller/laer-delete

chmod a+x laer-delete
chmod a+x laer
cp laer /usr/bin/laer
cp laer-delete /usr/bin/laer-delete

"""

Remove="""

laer-delete

"""
