Name="idur-stable"
Version="v0.0.1"
Depends=["curl", "bash", "python3", "coreutils"]

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Description="""
idur
"""


Install="""
cd /tmp/
rm -vrf idurtemp/
mkdir -p idurtemp/
cd idurtemp/
curl -LO https://raw.githubusercontent.com/idur-package/idur/v0.0.1/src/idur.py
chmod a+x idur.py
cp idur.py /usr/bin/idur
rm -vrf idurtemp/

"""

Remove="""
rm -vrf /usr/bin/idur
"""
