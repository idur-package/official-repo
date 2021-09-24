Name="idur-dev"
Version="v0.2.0"
Depends=["curl", "bash", "python3", "coreutils", "git"]


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
cd /tmp/
rm -vrf idurtemp/
mkdir -p idurtemp/
cd idurtemp/
curl -LO https://raw.githubusercontent.com/idur-package/idur/v0.2.0/src/idur.py
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

