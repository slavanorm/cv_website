# script-daemon @ cv_daemon.sh

# unit @ /etc/systemd/system/cv_website.service
cat cv_website.service.template | sed 's:__pwd__:'"$(pwd)"':' > /etc/systemd/system/cv_website.service

#To start the daemon you run
systemctl start cv_website.service

#To start at boot you enable it
systemctl enable cv_website.service

# source:
# https://unix.stackexchange.com/questions/426862/proper-way-to-run-shell-script-as-a-daemon
