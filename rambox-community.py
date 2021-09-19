
Name="rambox-community"
Version="0.7.9"


Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="both"


License="https://raw.githubusercontent.com/ramboxapp/community-edition/master/LICENSE"
idurDepends= ["idur-pkg"]
Conflict= ["rambox-community"]
Description="""
Free and Open Source messaging and emailing app that combines common web applications into one. 
"""

Install64="""
mkdir -p /opt/rambox-community
cd /opt/rambox-community
idur-pkg download https://github.com/ramboxapp/community-edition/releases/download/0.7.9/Rambox-0.7.9-linux-x86_64.AppImage
chmod a+x Rambox-0.7.9-linux-x86_64.AppImage
echo "#!/usr/bin/bash
cd /opt/rambox-community/
./Rambox-0.7.9-linux-x86_64.AppImage
" > /opt/rambox-community/rambox
chmod a+x /opt/rambox-community/rambox
ln /opt/rambox-community/rambox /usr/bin/rambox

idur-pkg download https://raw.githubusercontent.com/ramboxapp/community-edition/master/resources/logo/256x256.png
mv 256x256.png /usr/share/icons/hicolor/256x256/apps/rambox.png

echo "[Desktop Entry]
Name=Rambox
Exec=rambox
Icon=rambox
Categories=Network
Type=Application" > /usr/share/applications/rambox.desktop
chmod a+x /usr/share/applications/rambox.desktop
"""

Install32="""
mkdir -p /opt/rambox-community
cd /opt/rambox-community
idur-pkg download https://github.com/ramboxapp/community-edition/releases/download/0.7.9/Rambox-0.7.9-linux-i386.AppImage
chmod a+x Rambox-0.7.9-linux-i386.AppImage
echo "#!/usr/bin/bash
cd /opt/rambox-community/
./Rambox-0.7.9-linux-i386.AppImage
" > /opt/rambox-community/rambox
chmod a+x /opt/rambox-community/rambox
ln /opt/rambox-community/rambox /usr/bin/rambox
"""

Remove="""
idur-pkg rm /opt/rambox-community/
idur-pkg rm /usr/bin/rambox
idur-pkg rm /usr/share/icons/hicolor/256x256/apps/rambox.png
idur-pkg rm /usr/share/applications/rambox.desktop

"""
