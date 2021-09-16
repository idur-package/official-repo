Name="idur-dev"
Version="v0.0.7-dev"
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
curl -LO https://raw.githubusercontent.com/idur-package/idur/326ea27663539cf164670a350113fc07a787182d/src/idur.py
chmod a+x idur.py
cp idur.py /usr/bin/idur
rm -vrf idurtemp/

"""

Remove="""
rm -vrf /usr/bin/idur
"""

