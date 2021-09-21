
Name="batjump-canjam"
Version="1"


Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="both"


License="https://raw.githubusercontent.com/Can202/BatJump/main/LICENSE"
Depends = ["libxcursor1"]
idurDepends = ["idur-pkg"]
Conflict= ["batjump-canjam"]
Description="""
BatJump is a clone of flappy bird game, made to a jam
"""

Install64="""
idur-pkg tmp bjcj
cd /tmp/idur-bjcj-tmp/
idur-pkg download https://github.com/Can202/BatJump/releases/download/jam/Linux64.zip
unzip Linux64.zip
chmod a+x BatJump.x86_64

echo "#!/usr/bin/bash
cd /usr/lib64/batjump-canjam/
./BatJump.x86_64" > batjump-canjam

chmod a+x batjump-canjam
idur-pkg rm Linux64.zip

idur-pkg download https://raw.githubusercontent.com/Can202/BatJump/main/icon/icon.png
mkdir -p /usr/share/icons/hicolor/256x256/apps/
cp icon.png /usr/share/icons/hicolor/256x256/apps/batjump-canjam.png

echo "[Desktop Entry]
Name=BatJump
Exec=batjump-canjam
Icon=batjump-canjam
Type=Application
Categories=Game" > /usr/share/applications/batjump-canjam.desktop

mkdir -p /usr/lib64/batjump-canjam
cp /tmp/idur-bjcj-tmp/* /usr/lib64/batjump-canjam/

ln /usr/lib64/batjump-canjam/batjump-canjam /usr/bin/batjump-canjam


"""

Install32="""
idur-pkg tmp bjcj
cd /tmp/idur-bjcj-tmp/
idur-pkg download https://github.com/Can202/BatJump/releases/download/jam/Linux32.zip
unzip Linux32.zip
chmod a+x BatJump.x86

echo "#!/usr/bin/bash
cd /usr/lib32/batjump-canjam/
./BatJump.x86" > batjump-canjam

chmod a+x batjump-canjam
idur-pkg rm Linux32.zip

idur-pkg download https://raw.githubusercontent.com/Can202/BatJump/main/icon/icon.png
mkdir -p /usr/share/icons/hicolor/256x256/apps/
cp icon.png /usr/share/icons/hicolor/256x256/apps/batjump-canjam.png

echo "[Desktop Entry]
Name=BatJump
Exec=batjump-canjam
Icon=batjump-canjam
Type=Application
Categories=Game" > /usr/share/applications/batjump-canjam.desktop

mkdir -p /usr/lib32/batjump-canjam
cp /tmp/idur-bjcj-tmp/* /usr/lib32/batjump-canjam/

ln /usr/lib32/batjump-canjam/batjump-canjam /usr/bin/batjump-canjam



"""

Remove="""

idur-pkg rm /usr/lib64/batjump-canjam
idur-pkg rm /usr/lib32/batjump-canjam
idur-pkg rm /usr/bin/batjump-canjam
idur-pkg rm /usr/share/icons/hicolor/256x256/apps/batjump-canjam.png
idur-pkg rm /usr/share/applications/batjump-canjam.desktop

"""
