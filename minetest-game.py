Name="minetest-game"
Version="5.4.1"

Maintainer="Can202"
Contact="mgoopazo@gmail.com"
Time="medium"
Arch="all"


License="https://raw.githubusercontent.com/minetest/minetest/master/LICENSE.txt"
Depends=["libbz2-dev","libirrlicht-dev","dialog", "git", "g++", "make", "libc6-dev", "cmake", "libpng-dev", "libjpeg-dev", "libxxf86vm-dev", "libgl1-mesa-dev", "libsqlite3-dev", "libogg-dev", "libvorbis-dev", "libopenal-dev", "libcurl4-gnutls-dev", "libfreetype6-dev", "zlib1g-dev", "libgmp-dev", "libjsoncpp-dev", "libzstd-dev"]
idurDepends=["idur-pkg", "idur-exec"]
Conflict=["minetest-game"]
Description="""
An open source voxel game engine. Play one of our many games,
mod a game to your liking, make your own game, or play on a
multiplayer server.

Similar to Minecraft

(Compiled Version)

"""

Install="""

idur-pkg tmp minetest
cd $(idur-pkg dp minetest)
git clone --depth 1 --branch 5.4.1 https://github.com/minetest/minetest
cd minetest
git clone --depth 1 --branch 5.4.1 https://github.com/minetest/minetest_game games/minetest_game
# git clone --depth 1 https://github.com/minetest/irrlicht.git lib/irrlichtmt
cmake . -DRUN_IN_PLACE=TRUE
make -j$(nproc)
cd $(idur-pkg dp minetest)
cp -r minetest/ /opt/idur/

echo "#!/bin/bash
cd /opt/idur/minetest/
./bin/minetest
" > /opt/idur/bin/minetest-game
idur-pkg exec /opt/idur/bin/minetest-game
idur-pkg mod /opt/idur/minetest/
echo "[Desktop Entry]
Name=Minetest
Exec=idur-exec minetest-game
Icon=/opt/idur/minetest/games/minetest_game/menu/icon.png
Type=Application
Categories=Game" > /usr/share/applications/minetest-game.desktop
idur-pkg exec /usr/share/applications/minetest-game.desktop

idur-pkg rm-tmp minetest


"""

Remove="""

idur-pkg rm /opt/idur/minetest/
idur-pkg rm /opt/idur/bin/minetest-game
idur-pkg rm /usr/share/applications/minetest-game.desktop

"""
