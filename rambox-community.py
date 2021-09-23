
Name="rambox-community"
Version="0.7.9"

Time="short"
Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="both"


License="https://raw.githubusercontent.com/ramboxapp/community-edition/master/LICENSE"
idurDepends= ["idur-pkg", "idur-exec"]
Conflict= ["rambox-community"]
Description="""
Free and Open Source messaging and emailing app that combines common web applications into one. 
"""

Install64="""
mkdir -p /opt/idur/share/program/rambox-community
cd /opt/idur/share/program/rambox-community
idur-pkg download https://github.com/ramboxapp/community-edition/releases/download/0.7.9/Rambox-0.7.9-linux-x86_64.AppImage
idur-pkg exec Rambox-0.7.9-linux-x86_64.AppImage
echo "#!/usr/bin/bash
cd /opt/idur/share/program/rambox-community/
./Rambox-0.7.9-linux-x86_64.AppImage
" > /opt/idur/share/program/rambox-community/rambox
idur-pkg exec /opt/idur/share/program/rambox-community/rambox
ln /opt/idur/share/program/rambox-community/rambox /opt/idur/bin/rambox

idur-pkg download https://raw.githubusercontent.com/ramboxapp/community-edition/master/resources/logo/256x256.png
mv 256x256.png /opt/idur/share/icons/rambox.png

echo "[Desktop Entry]
Name=Rambox
Exec=idur-exec rambox
Icon=/opt/idur/share/icons/rambox.png
Categories=Network
Type=Application" > /usr/share/applications/rambox.desktop
idur-pkg exec /usr/share/applications/rambox.desktop
"""

Install32="""
mkdir -p /opt/idur/share/program/rambox-community
cd /opt/idur/share/program/rambox-community
idur-pkg download https://github.com/ramboxapp/community-edition/releases/download/0.7.9/Rambox-0.7.9-linux-i386.AppImage
idur-pkg exec Rambox-0.7.9-linux-i386.AppImage
echo "#!/usr/bin/bash
cd /opt/idur/share/program/rambox-community/
./Rambox-0.7.9-linux-i386.AppImage
" > /opt/idur/share/program/rambox-community/rambox
idur-pkg exec /opt/idur/share/program/rambox-community/rambox
ln /opt/idur/share/program/rambox-community/rambox /opt/idur/bin/rambox

idur-pkg download https://raw.githubusercontent.com/ramboxapp/community-edition/master/resources/logo/256x256.png
mv 256x256.png /opt/idur/share/icons/rambox.png

echo "[Desktop Entry]
Name=Rambox
Exec=idur-exec rambox
Icon=/opt/idur/share/icons/rambox.png
Categories=Network
Type=Application" > /usr/share/applications/rambox.desktop
idur-pkg exec /usr/share/applications/rambox.desktop
"""

Remove="""
idur-pkg rm /opt/idur/share/program/rambox-community/
idur-pkg rm /opt/idur/bin/rambox
idur-pkg rm /opt/idur/share/icons/rambox.png
idur-pkg rm /usr/share/applications/rambox.desktop

"""
