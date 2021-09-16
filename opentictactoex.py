Name="opentictactoex"
Version="v0.5"
Depends=["libxcursor1"]

Conflict=["xterm"]

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="both" #all, x86_64, i386, both

Description="""
opentictactoex
"""


Install64="""
cd /tmp/
rm -vrf otttxtemp/
mkdir -p otttxtemp/
cd otttxtemp/
curl -LO https://sourceforge.net/projects/opentictactoex/files/v0.5/OpenTicTacToeX.x86/download
curl -LO https://raw.githubusercontent.com/OpenTicTacToeX/package/main/deb64/usr/share/icons/hicolor/256x256/apps/opentictactoex.png
curl -LO https://raw.githubusercontent.com/OpenTicTacToeX/package/main/deb64/usr/share/applications/opentictactoex.desktop
chmod a+x opentictactoex.desktop
chmod a+x download
cp download /usr/bin/opentictactoex
cd ..
rm -vrf /tmp/otttxtemp/

"""

Install32="""
rm -vrf /tmp/otttxtemp/
mkdir -p /tmp/otttxtemp/
cd /tmp/otttxtemp/
curl -LO https://sourceforge.net/projects/opentictactoex/files/v0.5/OpenTicTacToeX.x86_64/download
curl -LO https://raw.githubusercontent.com/OpenTicTacToeX/package/main/deb64/usr/share/icons/hicolor/256x256/apps/opentictactoex.png
curl -LO https://raw.githubusercontent.com/OpenTicTacToeX/package/main/deb64/usr/share/applications/opentictactoex.desktop
chmod a+x opentictactoex.desktop
chmod a+x download 
cp opentictactoex.desktop /usr/share/applications/opentictactoex.desktop
cp opentictactoex.png /usr/share/icons/hicolor/256x256/apps/opentictactoex.png
cp download /usr/bin/opentictactoex
cd ..
rm -vrf /tmp/otttxtemp/

"""

Remove="""
rm -vrf /usr/bin/opentictactoex
rm -vrf /usr/share/applications/opentictactoex.desktop
rm -vrf /usr/share/icons/hicolor/256x256/apps/opentictactoex.png
"""

