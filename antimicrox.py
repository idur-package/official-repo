
Name="antimicrox"
Version="3.1.7"


Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="x86_64"


License="https://raw.githubusercontent.com/AntiMicroX/antimicrox/master/LICENSE"
idurDepends= ["idur-pkg"]
Conflict= ["antimicrox"]
Description="""
Graphical program used to map keyboard buttons and mouse controls to a gamepad. Useful for playing games with no gamepad support. 

"""

Install64="""

idur-pkg tmp amx
cd /tmp/idur-amx-tmp/
idur-pkg download https://github.com/AntiMicroX/antimicrox/releases/download/3.1.7/AntiMicroX-x86_64.AppImage
mkdir -p /opt/antimicrox
cp AntiMicroX-x86_64.AppImage /opt/antimicrox/antimicrox
chmod a+x /opt/antimicrox/antimicrox
ln /opt/antimicrox/antimicrox /usr/bin/antimicrox

"""

Remove="""

idur-pkg rm /opt/antimicrox/
idur-pkg rm /usr/bin/antimicrox

"""
