Name="minetest-game"
Version="5.4.1"

Maintainer="Can202"
Contact="mgoopazo@gmail.com"
Time="medium"
Arch="all"


License="https://raw.githubusercontent.com/minetest/minetest/master/LICENSE.txt"
Depends=["dialog", "git", "g++", "make", "libc6-dev", "cmake", "libpng-dev", "libjpeg-dev", "libxxf86vm-dev", "libgl1-mesa-dev", "libsqlite3-dev", "libogg-dev", "libvorbis-dev", "libopenal-dev", "libcurl4-gnutls-dev", "libfreetype6-dev", "zlib1g-dev", "libgmp-dev", "libjsoncpp-dev", "libzstd-dev"]
idurDepends=["idur-pkg"]
Conflict=["minetest-game"]
Description="""
An open source voxel game engine. Play one of our many games,
mod a game to your liking, make your own game, or play on a
multiplayer server.

Similar to Minecraft

(Compiled Version)

"""

Install="""

dialog --title "Compile minetest" --yesno "This version is compiled, are you sure that you want to compile the game?, this takes time" 0 0
if [ $? = 0 ]
then
    idur-pkg tmp minetest
    cd $(idur-pkg dp minetest)
    git clone --depth 1 https://github.com/minetest/minetest
    cd minetest
    git checkout 5.4.1
    git clone --depth 1 --branch 5.4.1 https://github.com/minetest/minetest_game games/minetest_game
    git clone --depth 1 https://github.com/minetest/irrlicht.git lib/irrlichtmt
    cmake . -DRUN_IN_PLACE=TRUE
    make -j$(nproc)
    cd $(idur-pkg dp minetest)
    cp -r minetest/ /opt/
    

    echo "#!/bin/bash
    cd /opt/minetest/
    ./bin/minetest
    " > /usr/bin/minetest-game
    chmod a+x /usr/bin/minetest-game
    chmod a+rwx -R /opt/minetest/
    echo "[Desktop Entry]
Name=Minetest
Exec=minetest-game
Icon=/opt/minetest/games/minetest_game/menu/icon.png
Type=Application
Categories=Game" > /usr/share/applications/minetest-game.desktop
    chmod a+x /usr/share/applications/minetest-game.desktop

else
    clear
    echo "aborting"
fi


idur-pkg rm-tmp minetest


"""

Remove="""

idur-pkg rm /opt/minetest/
idur-pkg rm /usr/bin/minetest-game
idur-pkg rm /usr/share/applications/minetest-game.desktop

"""
