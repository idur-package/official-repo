
Name="idur-pkg"
Version="v0.6"

Time="short"
Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="all"

Depends= ["curl", "coreutils"]
idurDepends=["dunpress"]
Conflict= ["idur-pkg"]
Description="""
idur dev tools

"""

Install="""
curl -L https://raw.githubusercontent.com/idur-package/idur-pkg/v0.6/idur-pkg > /usr/bin/idur-pkg
chmod a+x /usr/bin/idur-pkg

"""

Remove="""

rm -vrf /usr/bin/idur-pkg

"""
