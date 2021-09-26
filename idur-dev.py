Name="idur-dev"
Version="v0.2.3-dev-1"
Depends=["curl", "bash", "python3", "python3-pip", "coreutils", "git"]


Conflict=["idur-stable", "idur-dev"]
Time="short"
Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="all" #all, x86_64, i386, both

Description="""
idur is a community package manager to debian systems (ubuntu-based too)

Like an AUR, but more simple.

idur-dev is the developer version, to test it
NOT INSTALL
"""


Install="""

pip3 install colorama

cd /tmp/
rm -vrf idurtemp/
mkdir -p idurtemp/
cd idurtemp/
curl -LO https://raw.githubusercontent.com/idur-package/idur/d3b0d903acb4c5b44ff53fa0d74618cadf044305/src/idur.py
chmod a+x idur.py
cp idur.py /usr/bin/idur
rm -vrf idurtemp/

idur install idur-pkg
echo
echo
echo
echo "installed with no problem!"

"""

Remove="""
rm -vrf /usr/bin/idur
"""

