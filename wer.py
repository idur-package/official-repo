Name="wer"
Version=0.5
Depends=["python3", "bash", "curl"]


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
