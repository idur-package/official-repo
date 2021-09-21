
Name="nullpomino"
Version="v7.5.0"


Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="x86_64"


License="https://raw.githubusercontent.com/nullpomino/nullpomino/master/LICENSE"
Depends=["unzip"]
idurDepends= ["idur-pkg", "openjdk-17"]
Conflict= ["nullpomino"]
Description="""
An action puzzle game like the popular Tetris game
"""

Install64="""
if [[ "lala" = "broke" ]]
then
	echo "hello"
fi
idur-pkg tmp nullpomino
cd /tmp/idur-nullpomino-tmp/
idur-pkg download https://github.com/nullpomino/nullpomino/releases/download/v7.5.0/NullpoMino7.5.0.zip
unzip NullpoMino7.5.0.zip
cp -vr NullpoMino7_5_0/ /opt/nullpomino
idur-pkg read https://raw.githubusercontent.com/idur-package/media/8b0a85ae4430dabaae826496c0d4faef6755902b/nullpomino/play_swing > /opt/nullpomino/play
idur-pkg read https://raw.githubusercontent.com/idur-package/media/6181b2b223f8ab2e4309db7015b0d82f35c727d7/nullpomino/nullpomino > /usr/bin/nullpomino
chmod a+x /usr/bin/nullpomino
chmod a+x /opt/nullpomino/play

idur-pkg download https://raw.githubusercontent.com/idur-package/media/678e5948e48f27f542d82cac1a84b08af0598a2b/nullpomino/nullpomino.png
cp nullpomino.png /opt/nullpomino/nullpomino.png

idur-pkg read https://raw.githubusercontent.com/idur-package/media/678e5948e48f27f542d82cac1a84b08af0598a2b/nullpomino/nullpomino.desktop > /usr/share/applications/nullpomino.desktop
chmod a+x /usr/share/applications/nullpomino.desktop


idur-pkg rm-tmp nullpomino

"""

Remove="""
idur-pkg rm /opt/nullpomino/
idur-pkg rm /usr/bin/nullpomino

"""
