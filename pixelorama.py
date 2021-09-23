
Name="pixelorama"
Version="v0.9"


Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="x86_64"
Time="short"

License="https://raw.githubusercontent.com/Orama-Interactive/Pixelorama/master/LICENSE"
Depends= ["libxcursor1", "tar", "coreutils"]
idurDepends= ["idur-pkg", "idur-exec"]
Conflict= ["pixelorama"]
Description="""
A free & open-source 2D sprite editor, made with the Godot Engine! 

"""

Install64="""
idur-pkg tmp pixelorama
cd $(idur-pkg dp pixelorama)
idur-pkg download https://github.com/Orama-Interactive/Pixelorama/releases/download/v0.9/Pixelorama.Linux-64bit.tar.gz
idur-pkg uncompress Pixelorama.Linux-64bit.tar.gz
idur-pkg rm Pixelorama.Linux-64bit.tar.gz
mv linux-64bit/ pixelorama
idur-pkg copy pixelorama/ /opt/idur/share/program/
echo "#!/bin/bash
cd /opt/idur/share/program/pixelorama/
./Pixelorama.x86_64" > /opt/idur/bin/pixelorama
idur-pkg exec /opt/idur/bin/pixelorama
idur-pkg download https://raw.githubusercontent.com/Orama-Interactive/Pixelorama/master/assets/graphics/icons/icon.png
idur-pkg copy icon.png /opt/idur/share/icons/pixelorama.png
echo "[Desktop Entry]
Name=Pixelorama
Exec=idur-exec pixelorama
Icon=/opt/idur/share/icons/pixelorama.png
Type=Application
Categories=Graphics;2DGraphics;" > /usr/share/applications/pixelorama.desktop
idur-pkg exec /usr/share/applications/pixelorama.desktop
idur-pkg rm-tmp pixelorama
"""

Remove="""

idur-pkg rm /opt/idur/share/program/pixelorama/Pixelorama.x86_64
idur-pkg rm /opt/idur/share/program/pixelorama/Pixelorama.pck
idur-pkg rm /usr/share/applications/pixelorama.desktop
idur-pkg rm /opt/idur/share/icons/pixelorama.png
idur-pkg rm /opt/idur/bin/pixelorama

"""
