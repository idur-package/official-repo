Name="tcs-cleaner"
Version=0
Depends=["curl", "bash"]


Install="""
curl https://raw.githubusercontent.com/Can202/tcs-cleaner/main/installer | bash

"""

Remove="""
tcs-cleaner-remove
"""
