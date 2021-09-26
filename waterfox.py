Name="waterfox"
Version="Auto2"

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="x86_64"
Time="almost-medium"

License="https://github.com/WaterfoxCo/Waterfox/blob/current/LICENSE"
idurDepends=["idur-pkg", "idur-exec"]
Conflict=["waterfox"]
Description="""
Web Browser
Waterfox:
The way to surf the web.
Striking the perfect balance of privacy and useability. 
based on Firefox

"""

Install64="""
idur-pkg tmp waterfox
cd $(idur-pkg dp waterfox)
idur-pkg download https://cdn.waterfox.net/releases/linux64/installer/waterfox-G3.2.6.en-US.linux-x86_64.tar.bz2
idur-pkg uncompress waterfox-G3.2.6.en-US.linux-x86_64.tar.bz2
cp -r waterfox /opt/idur/share/program/
chmod a+rw -R /opt/idur/share/program/waterfox
echo "#!/usr/bin/bash
other="\$1 \$2 \$3 \$4 \$5 \$6 \$7 \$8 \$9"
cd /opt/idur/share/program/waterfox
./waterfox \$other" > /opt/idur/bin/waterfox
chmod a+x /opt/idur/bin/waterfox
echo "[Desktop Entry]
Name=Waterfox
Exec=idur-exec waterfox
Type=Application
Icon=/opt/idur/share/program/waterfox/browser/chrome/icons/default/default128.png
Categories=Network" > /usr/share/applications/waterfox.desktop
chmod a+x /usr/share/applications/waterfox.desktop
idur-pkg rm-tmp waterfox

"""

Remove="""
idur-pkg rm /opt/idur/share/program/waterfox/
idur-pkg rm /opt/idur/bin/waterfox
idur-pkg rm /usr/share/applications/waterfox.desktop
"""
