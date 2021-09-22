
Name="dgitignore"
Version="v0.1"

Time="short"
Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="all"


License="https://raw.githubusercontent.com/Can202/dgitignore/master/LICENSE"
Depends= ["git", "coreutils", "python3", "curl"]
Conflict= ["dgitignore"]
Description="""
dgitignore program to use the gitignore templates

"""

Install="""
rm -vrf /usr/bin/dgitignore
echo "$(curl https://raw.githubusercontent.com/Can202/dgitignore/v0.1/dgitignore.py)" > /usr/bin/dgitignore
chmod a+x /usr/bin/dgitignore

"""

Remove="""

rm -vrf /usr/bin/dgitignore

"""
