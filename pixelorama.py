
Name="pixelorama"
Version="v0.9"


Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="x86_64"
Time="short"

License="https://raw.githubusercontent.com/Orama-Interactive/Pixelorama/master/LICENSE"
Depends= ["libxcursor1", "tar", "coreutils"]
idurDepends= ["idur-pkg"]
Conflict= ["pixelorama"]
Description="""
A free & open-source 2D sprite editor, made with the Godot Engine! 

"""

Install64="""
idur-pkg tmp pixelorama
cd /tmp/idur-pixelorama-tmp
idur-pkg download https://github.com/Orama-Interactive/Pixelorama/releases/download/v0.9/Pixelorama.Linux-64bit.tar.gz
tar -xvzf Pixelorama.Linux-64bit.tar.gz
idur-pkg rm Pixelorama.Linux-64bit.tar.gz
mv linux-64bit/ pixelorama
cp -r pixelorama/ /usr/lib64/
echo "#!/bin/bash
cd /usr/lib64/pixelorama/
./Pixelorama.x86_64" > /usr/bin/pixelorama
chmod a+x /usr/bin/pixelorama
idur-pkg download https://raw.githubusercontent.com/Orama-Interactive/Pixelorama/master/assets/graphics/icons/icon.png
cp icon.png /usr/share/icons/hicolor/256x256/apps/pixelorama.png
echo "[Desktop Entry]
Name=Pixelorama
Exec=pixelorama
Icon=pixelorama
Type=Application
Categories=Graphics;2DGraphics;" > /usr/share/applications/pixelorama.desktop
chmod a+x /usr/share/applications/pixelorama.desktop
"""

Remove="""

idur-pkg rm /usr/lib64/pixelorama/Pixelorama.x86_64
idur-pkg rm /usr/lib64/pixelorama/Pixelorama.pck
idur-pkg rm /usr/share/applications/pixelorama.desktop
idur-pkg rm /usr/share/icons/hicolor/256x256/apps/pixelorama.png
idur-pkg rm /usr/bin/pixelorama

"""
