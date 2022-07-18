Name="soundux"
Version="v0.2.7"

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="x86_64"

Time="long"


License="https://raw.githubusercontent.com/Soundux/Soundux/master/LICENSE"
Depends=["git", "build-essential", "cmake", "libx11-dev", "libxi-dev", "libwebkit2gtk-4.0-dev", "libssl-dev", "libpulse-dev", "libpipewire-0.3-dev"]
idurDepends=["idur-pkg", "idur-exec"]
Conflict=["soundux"]
Description="""
A cross-platform soundboard

"""

Install64="""
# Install instructions here (bash)

# Temp Directory
idur-pkg tmp soundux
cd $(idur-pkg dp soundux)

# Depends  "libappindicator3-dev"
mkdir depends
cd depends
idur-pkg download http://ftp.us.debian.org/debian/pool/main/liba/libappindicator/gir1.2-appindicator3-0.1_0.4.92-7_amd64.deb
idur-pkg download http://ftp.us.debian.org/debian/pool/main/libi/libindicator/libindicator3-7_0.5.0-4_amd64.deb
idur-pkg download http://ftp.us.debian.org/debian/pool/main/liba/libappindicator/libappindicator3-dev_0.4.92-7_amd64.deb
idur-pkg download http://ftp.us.debian.org/debian/pool/main/liba/libappindicator/libappindicator3-1_0.4.92-7_amd64.deb
apt install ./*
cd ..

# Download Files
idur-pkg download https://github.com/Soundux/Soundux/releases/download/0.2.7/soundux-0.2.7.tar.gz
idur-pkg uncompress soundux-0.2.7.tar.gz

# Build
cd Soundux/
mkdir build
cd build
cmake ..
cmake --build . --config Release
cd ..




# Copy Files
idur-pkg copy build /opt/soundux
idur-pkg copy assets/icon_squared.png /opt/idur/share/icons/soundux.png

# Make Executable (chmod a+x)
echo "#!/usr/bin/bash
cd /opt/soundux
./soundux --reset-mutex" > /opt/idur/bin/soundux
idur-pkg exec /opt/idur/bin/soundux

echo "[Desktop Entry]
Name=Soundux
Exec=idur-exec soundux
Type=Application
Icon=/opt/idur/share/icons/soundux.png
Categories=AudioVideo;Audio;AudioVideoEditing;" > /usr/share/applications/soundux-idur.desktop
idur-pkg exec /usr/share/applications/soundux-idur.desktop
chmod a+rwx -R /opt/soundux/


# Remove Temp Directory
idur-pkg rm-tmp soundux

"""

Remove="""
# Remove instructions here (bash)
idur-pkg rm-tmp soundux
idur-pkg rm /usr/share/applications/soundux-idur.desktop
idur-pkg rm /opt/soundux/
idur-pkg rm /opt/idur/share/icons/soundux.png

"""
