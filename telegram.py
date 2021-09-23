Name="telegram"
Version="automatic.2"

Maintainer="Can202"
Contact="mgoopazo@gmail.com"
Time="short"
Arch="x86_64"


License="https://raw.githubusercontent.com/telegramdesktop/tdesktop/dev/LICENSE"
idurDepends=["idur-pkg", "idur-exec"]
Conflict=["telegram", "telegram-desktop"]
Description="""
Telegram Desktop:
(Automatic Updater)
Fast and secure desktop app,
perfectly synced with your
mobile phone.

"""

Install64="""
idur-pkg tmp tl
cd $(idur-pkg dp tl)
idur-pkg download https://telegram.org/dl/desktop/linux
mv linux linux.tar.xz
idur-pkg uncompress linux.tar.xz
cp -r Telegram/ /opt/idur/share/program/

idur-pkg download https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Telegram_2019_Logo.svg/150px-Telegram_2019_Logo.svg.png
cp 150px-Telegram_2019_Logo.svg.png /opt/idur/share/icons/telegram.png

echo "#!/usr/bin/bash
cd /opt/idur/share/program/Telegram/
./Updater" > /opt/idur/bin/telegram
chmod a+x /opt/idur/bin/telegram

echo "[Desktop Entry]
Name=Telegram
Exec=idur-exec telegram
Type=Application
Icon=/opt/idur/share/icons/telegram.png
Categories=Network" > /usr/share/applications/telegram.desktop
chmod a+x /usr/share/applications/telegram.desktop
chmod a+rwx -R /opt/idur/share/program/Telegram/

idur-pkg rm-tmp tl
"""

Remove="""
idur-pkg rm /usr/share/applications/telegram.desktop
idur-pkg rm /opt/idur/share/program/Telegram/
idur-pkg rm /opt/idur/bin/telegram
idur-pkg rm /opt/idur/share/icons/telegram.png

"""
