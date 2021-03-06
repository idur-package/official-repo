
Name="create-idur"
Version="v0.8"

Time="short"
Maintainer="Can202"
Contact="mgoopazo@gmail.com"

Arch="all"

Depends= ["python3", "coreutils", "curl", "rec/idur-stable idur-dev"]
Conflict= ["create-idur"]
idurDepends=["idur-pkg"]
Description="""

An Easy way to create idurs

"""

Install="""

cd /tmp/
rm -vrf create-idur.py
curl -LO https://raw.githubusercontent.com/idur-package/create-idur/v0.8/create-idur.py
chmod a+x create-idur.py
cp create-idur.py /usr/bin/create-idur

"""

Remove="""

rm -vrf /usr/bin/create-idur

"""
