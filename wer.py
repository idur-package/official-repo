Name="wer"
Version="0.5"
Depends=["python3", "bash", "curl"]
idurDepends=["idur-pkg"]
Conflict=["wer"]

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"
License="https://raw.githubusercontent.com/Can202/wer/main/LICENSE"

Time="short"

Arch="all" #all, x86_64, i386, both

Description="""
wer is a program to read files with terminal, an alternative
to cat, but also it can create plain/text files, write quick
phrases on file, clear the windows, check if the file exists,
remove files and list directories.
"""


Install="""
idur-pkg read https://raw.githubusercontent.com/Can202/wer/0.5/wer.py > /usr/bin/wer
idur-pkg exec /usr/bin/wer
"""

Remove="""
idur-pkg rm /usr/bin/wer
"""
