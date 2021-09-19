
Name="neteja"
Version="V4.0"


Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="all"


License="https://gitlab.com/voromv/Neteja/-/raw/main/LICENSE"
Depends= ["dialog", "sudo", "coreutils", "bash", "curl", "tar"]
Conflict= ["neteja"]
Description="""
Neteja es un script de limpieza para linux, hecho por Voro MV y su comunidad.
"""

Install="""
cd /tmp/
rm -vrf netejatemp
mkdir -p netejatemp
cd netejatemp

curl -LO https://gitlab.com/voromv/Neteja/-/archive/V4.0/Neteja-V4.0.tar
tar -xvf Neteja-V4.0.tar

chmod a+x Neteja-V4.0/*


cp -r Neteja-V4.0 /usr/lib/neteja


echo "cd /usr/lib/neteja/
./neteja.sh" > /usr/lib/neteja/neteja
chmod a+x /usr/lib/neteja/neteja

ln /usr/lib/neteja/neteja /usr/bin/neteja



cd ..
rm -vrf netejatemp

"""

Remove="""
rm -vrf /usr/bin/neteja
rm -vrf /usr/lib/neteja/
# Remove instructions here (bash)

"""
