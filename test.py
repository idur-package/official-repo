Name="test"
Version="0.5"
Depends=["python3", "bash", "curl", "rec/xterm lxterminal"]
idurDepends=["idur-stable idur-dev"]
Conflict=["wer", "test"]

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"
License="https://raw.githubusercontent.com/Can202/wer/main/LICENSE"

Arch="all" #all, x86_64, i386, both

Description="""
wer is a program to read file with terminal
"""


Install="""

rm -vrf /tmp/wertmp/

cd /tmp/
mkdir -p wertmp/
cd wertmp/
curl -LO https://raw.githubusercontent.com/Can202/wer/0.5/wer.py

chmod a+x wer.py

cp wer.py /usr/bin/wer


rm -vrf /tmp/wertmp/

"""

Remove="""
rm -vrf /usr/bin/wer
"""
