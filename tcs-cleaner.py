Name="tcs-cleaner"
Version="0"
Depends=["curl", "bash", "dialog", "coreutils", "sug/snapd", "sug/flatpak"]
Conflict=["tcs-cleaner"]
Time="short"
Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="all" #all, x86_64, i386, both

Description="""
tcs-cleaner is a system cleaner script, Update your system, remove temp data,
cache files if I spend a long time without being used and remove logs.
"""

Install="""#!/usr/bin/bash
if [ ! $(whoami) = "root" ]
then
    if [ -f "/usr/bin/dialog" ] || [ -f "/usr/sbin/dialog" ] || [ -f "/usr/games/dialog" ]
    then
        dialog --title "root" --msgbox "You need run this script as root" 0 0
    else
        echo "You need run this script as root"
    fi
    clear
    exit
fi
version=$(curl https://raw.githubusercontent.com/Can202/tcs-cleaner/main/version)

echo "remove tcs-cleaner if it's installed"
rm -vrf /usr/bin/tcs-cleaner
rm -vrf /usr/bin/tcs-cleaner-remove


echo "getting $version version of tcs-cleaner"
cd /tmp/
rm -vrf tcs-cleaner
mkdir -p tcs-cleaner
cd tcs-cleaner/

curl -LO https://raw.githubusercontent.com/Can202/tcs-cleaner/$version/tcs-cleaner
chmod a+x tcs-cleaner
cp tcs-cleaner /usr/bin/tcs-cleaner

curl -LO https://raw.githubusercontent.com/Can202/tcs-cleaner/$version/tcs-cleaner-remove
chmod a+x tcs-cleaner-remove
cp tcs-cleaner-remove /usr/bin/tcs-cleaner-remove


curl -LO https://raw.githubusercontent.com/Can202/tcs-cleaner/$version/desktops/tcs-cleaner.png
cp tcs-cleaner.png /usr/share/icons/hicolor/256x256/apps/tcs-cleaner.png


curl -LO https://raw.githubusercontent.com/Can202/tcs-cleaner/$version/desktops/tcs-cleaner-su.desktop
curl -LO https://raw.githubusercontent.com/Can202/tcs-cleaner/$version/desktops/tcs-cleaner-sudo.desktop
curl -LO https://raw.githubusercontent.com/Can202/tcs-cleaner/$version/desktops/tcs-cleaner.desktop
chmod a+x tcs-cleaner-su.desktop
chmod a+x tcs-cleaner-sudo.desktop
chmod a+x tcs-cleaner.desktop
cp tcs-cleaner.desktop /usr/share/applications/
cp tcs-cleaner-sudo.desktop /usr/share/applications/
cp tcs-cleaner-su.desktop /usr/share/applications/



"""

Remove="""
tcs-cleaner-remove
"""
