Name="opentictactoex"
Version="v0.5-1"
Depends=["libxcursor1"]
idurDepends=["idur-pkg", "idur-exec"]
Conflict=["opentictactoex"]

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="both" #all, x86_64, i386, both
Time="almost-medium"
Description="""
opentictactoex, a simple Tic Tac Toe game to play with a friend.
"""


Install64="""
idur-pkg tmp otttx
cd $(idur-pkg dp otttx)
idur-pkg download https://sourceforge.net/projects/opentictactoex/files/v0.5/OpenTicTacToeX.x86_64/download
idur-pkg download https://raw.githubusercontent.com/OpenTicTacToeX/package/main/deb64/usr/share/icons/hicolor/256x256/apps/opentictactoex.png
cp opentictactoex.png /opt/idur/share/icons/opentictactoex.png
idur-pkg exec download
cp download /opt/idur/bin/opentictactoex
echo "[Desktop Entry]
Name=OpenTicTacToeX
Exec=idur-exec opentictactoex
Icon=/opt/idur/share/icons/opentictactoex.png
Type=Application
Categories=Game" > /usr/share/applications/opentictactoex.desktop
idur-pkg exec /usr/share/applications/opentictactoex.desktop
idur-pkg rm-tmp otttx
"""

Install32="""
idur-pkg tmp otttx
cd $(idur-pkg dp otttx)
idur-pkg download https://sourceforge.net/projects/opentictactoex/files/v0.5/OpenTicTacToeX.x86/download
idur-pkg download https://raw.githubusercontent.com/OpenTicTacToeX/package/main/deb64/usr/share/icons/hicolor/256x256/apps/opentictactoex.png
cp opentictactoex.png /opt/idur/share/icons/opentictactoex.png
idur-pkg exec download
cp download /opt/idur/bin/opentictactoex
echo "[Desktop Entry]
Name=OpenTicTacToeX
Exec=idur-exec opentictactoex
Icon=/opt/idur/share/icons/opentictactoex.png
Type=Application
Categories=Game" > /usr/share/applications/opentictactoex.desktop
idur-pkg exec /usr/share/applications/opentictactoex.desktop
idur-pkg rm-tmp otttx
"""

Remove="""
idur-pkg rm /opt/idur/bin/opentictactoex
idur-pkg rm /usr/share/applications/opentictactoex.desktop
idur-pkg rm /opt/idur/share/icons/opentictactoex.png
"""

