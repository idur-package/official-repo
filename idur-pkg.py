
Name="idur-pkg"
Version="v0.3"


Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="all"

Depends= ["curl", "coreutils"]
Conflict= ["idur-pkg"]
Description="""
idur dev tools

"""

Install="""

curl -L https://raw.githubusercontent.com/Can202/idur-pkg/v0.3/idur-pkg > /usr/bin/idur-pkg
chmod a+x /usr/bin/idur-pkg

"""

Remove="""

rm -vrf /usr/bin/idur-pkg

"""
