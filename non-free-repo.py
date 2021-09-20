
Name="non-free-repo"
Version="1"


Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="all"

idurDepends= ["idur-stable idur-dev"]
Conflict= ["non-free-repo"]
Description="""
active the non-free-repo to get programs non free software

"""

Install="""
idur add-repo non-free-repo https://github.com/idur-package/non-free-repo
"""

Remove="""

idur remove-repo non-free-repo 

"""
