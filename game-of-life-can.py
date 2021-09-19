
Name="game-of-life-can"
Version="v1"


Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="both"


License="https://raw.githubusercontent.com/Can202/GameOfLifeGodot/main/LICENSE"
Depends = ["libxcursor1"]
idurDepends= ["idur-pkg"]
Conflict= ["game-of-life-can"]
Description="""
The Game of Life by John Horton Conway created on Godot

"""

Install64="""
idur-pkg tmp golc
cd /tmp/idur-golc-tmp/
idur-pkg download https://github.com/Can202/GameOfLifeGodot/releases/download/v1/linux64.zip
unzip linux64.zip
chmod a+x GameOfLife.x86_64

echo "#!/usr/bin/bash
cd /usr/lib64/game-of-life-can/
./GameOfLife.x86_64" > game-of-life-can

chmod a+x game-of-life-can
idur-pkg rm linux64.zip

idur-pkg download https://raw.githubusercontent.com/Can202/GameOfLifeGodot/main/icon/icon.png
mkdir -p /usr/share/icons/hicolor/256x256/apps/
cp icon.png /usr/share/icons/hicolor/256x256/apps/game-of-life-can.png

echo "
[Desktop Entry]
Name=Game of Life
Exec=game-of-life-can
Icon=game-of-life-can
Type=Application
Categories=Game" > /usr/share/applications/game-of-life-can.desktop

mkdir -p /usr/lib64/game-of-life-can
cp * /usr/lib64/game-of-life-can/

ln /usr/lib64/game-of-life-can/game-of-life-can /usr/bin/game-of-life-can

"""

Install32="""

idur-pkg tmp golc
cd /tmp/idur-golc-tmp/
idur-pkg download https://github.com/Can202/GameOfLifeGodot/releases/download/v1/linux32.zip
unzip linux32.zip
chmod a+x GameOfLife.x86

echo "#!/usr/bin/bash
cd /usr/lib32/game-of-life-can/
./GameOfLife.x86" > game-of-life-can

chmod a+x game-of-life-can
idur-pkg rm linux32.zip

idur-pkg download https://raw.githubusercontent.com/Can202/GameOfLifeGodot/main/icon/icon.png
mkdir -p /usr/share/icons/hicolor/256x256/apps/
cp icon.png /usr/share/icons/hicolor/256x256/apps/game-of-life-can.png

echo "
[Desktop Entry]
Name=Game of Life
Exec=game-of-life-can
Icon=game-of-life-can
Type=Application
Categories=Game" > /usr/share/applications/game-of-life-can.desktop

mkdir -p /usr/lib32/game-of-life-can
cp * /usr/lib32/game-of-life-can/

ln /usr/lib32/game-of-life-can/game-of-life-can /usr/bin/game-of-life-can


"""

Remove="""

idur-pkg rm /usr/lib64/game-of-life-can
idur-pkg rm /usr/lib32/game-of-life-can
idur-pkg rm /usr/bin/game-of-life-can
idur-pkg rm /usr/share/icons/hicolor/256x256/apps/game-of-life-can.png
idur-pkg rm /usr/share/applications/game-of-life-can.desktop

"""
