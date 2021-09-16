Name="tcs-cleaner"
Version="0"
Depends=["curl", "bash"]
Conflict=["tcs-cleaner"]

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

Arch="all" #all, x86_64, i386, both

Description="""
tcs-cleaner
"""

Install="""
curl https://raw.githubusercontent.com/Can202/tcs-cleaner/main/installer | bash

"""

Remove="""
tcs-cleaner-remove
"""
