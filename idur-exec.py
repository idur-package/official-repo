Name="idur-exec"
Version="v0.2-2"
Depends=["python3", "bash", "curl"]
idurDepends=["idur-pkg"]
Conflict=["idur-exec"]

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"
License="https://raw.githubusercontent.com/idur-package/idur-exec/master/LICENSE"

Time="short"

Arch="all" #all, x86_64, i386, both

Description="""
idur-exec
"""


Install="""
mkdir -p /opt/
mkdir -p /opt/idur
mkdir -p /opt/idur/bin/
mkdir -p /opt/idur/share/
mkdir -p /opt/idur/share/program
mkdir -p /opt/idur/share/icons
echo "exec idur-exec program to execute /opt/idur/bin/program" > /opt/idur/bin/readme.txt
idur-pkg read https://raw.githubusercontent.com/idur-package/idur-exec/v0.2/idur-exec > /usr/bin/idur-exec
idur-pkg exec /usr/bin/idur-exec
"""

Remove="""
idur-pkg rm /usr/bin/idur-exec
"""
