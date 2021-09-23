
Name="openjdk-17"
Version="35.3"


Maintainer="Can202"
Contact="mgoopazo@hotmail.com"
Time="short"
Arch="x86_64"


License="https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt"
Depends=["tar", "python3"]
idurDepends= ["idur-pkg", "idur-exec"]
Conflict= ["openjdk-17"]
Description="""
openjdk-17, jre and jdk

"""

Install64="""
idur-pkg tmp jdk17
cd $(idur-pkg dp jdk17)
idur-pkg download https://download.java.net/java/GA/jdk17/0d483333a00540d886896bac774ff48b/35/GPL/openjdk-17_linux-x64_bin.tar.gz
idur-pkg uncompress openjdk-17_linux-x64_bin.tar.gz
idur-pkg copy /tmp/idur-jdk17-tmp/jdk-17/ /opt/idur/share/program/openjdk-17
idur-pkg read https://raw.githubusercontent.com/idur-package/media/ae4609fd1417f6fa91d71cade4dfadc2df59ec8f/openjdk-17/openjdk-17 > /opt/idur/bin/openjdk-17
idur-pkg exec /opt/idur/bin/openjdk-17
ln /opt/idur/bin/openjdk-17 /usr/bin/openjdk-17
idur-pkg rm-tmp jdk17
"""

Remove="""
idur-pkg rm /opt/idur/share/program/openjdk-17
idur-pkg rm /opt/idur/bin/openjdk-17
idur-pkg rm /usr/bin/openjdk-17

"""
