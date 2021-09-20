Name="dunpress"
Version="v0.2"

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="all"


License="https://raw.githubusercontent.com/Can202/dunpress/main/LICENSE"
Depends=["unzip", "tar", "python3"]
Conflict=["dunpress"]
Description="""
uncompress tarballs and zip with one command.

"""

Install="""

curl -L https://raw.githubusercontent.com/Can202/dunpress/v0.2/src/dunpress.py > /usr/bin/dunpress
chmod a+x /usr/bin/dunpress

"""

Remove="""

rm -vrf /usr/bin/dunpress

"""
