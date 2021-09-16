Name="tcs-cleaner"
Version="0"
Depends=["curl", "bash"]

Maintainer="Can202"
Contact="mgoopazo@hotmail.com"

x86_64="normal"
i386="normal"

Description="""
tcs-cleaner
"""

Install="""
curl https://raw.githubusercontent.com/Can202/tcs-cleaner/main/installer | bash

"""

Remove="""
tcs-cleaner-remove
"""
