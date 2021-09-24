Name="idt"
Version="1"

Maintainer="Can202"
Contact="mgoopazo@gmail.com"

Arch="all"

Time="short"

Depends=["coreutils"]
idurDepends=["idur-pkg", "idur-exec", "create-idur"]
Conflict=["idt"]
Description="""
Idur Dev Tools
Mega-Package that contains
Dev Tools to make idurs like....

idur-pkg - command line helper
(remove, download, make
executable, allow modify
files, copy, etc)

idur-exec - command to execute programs in /opt/idur/bin/

create-idur - command to create templates of idurs
"""

Install="""
echo "Dev tools installed"
"""

Remove="""
echo "you can remove the packages if a package need it"
echo "trying remove idur-pkg"
idur rm idur-pkg
echo "trying remove idur-exec"
idur rm idur-exec
echo "trying remove create-idur"
idur rm create-idur
"""
