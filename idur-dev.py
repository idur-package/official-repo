Name="idur-dev"
Version="v0.0.8-dev"
Depends=["curl", "bash", "python3", "coreutils", "git"]

Conflict=["idur-stable", "idur-dev"]

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="all" #all, x86_64, i386, both

Description="""
idur
"""


Install="""
cd /tmp/
rm -vrf idurtemp/
mkdir -p idurtemp/
cd idurtemp/
curl -LO https://raw.githubusercontent.com/idur-package/idur/3e1d37b2fa3f72e45c561c8d6b5041e040ba5cb6/src/idur.py
chmod a+x idur.py
cp idur.py /usr/bin/idur
rm -vrf idurtemp/

"""

Remove="""
rm -vrf /usr/bin/idur
"""

