Name="idur-dev"
Version="v0.1.4-dev"
Depends=["curl", "bash", "python3", "coreutils", "git"]


Conflict=["idur-stable", "idur-dev"]

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
curl -LO https://raw.githubusercontent.com/idur-package/idur/3e5a7935f859d3fd9dc4bd01a3f33acc503f650c/src/idur.py
chmod a+x idur.py
cp idur.py /usr/bin/idur
rm -vrf idurtemp/

idur install idur-pkg

"""

Remove="""
rm -vrf /usr/bin/idur
"""

