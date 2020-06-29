# daemon cv_daemon.sh
cat cv_daemon.sh.template | sed  's:__pwd__:'"$(pwd)"':' > cv_daemon.sh
# unit cv_website.service
cat cv_website.service.template | sed 's:__pwd__:'"$(pwd)"':' > cv_website.service

chmod 755 cv_daemon.sh
chmod 755 cv_website.service

cp cv_website.service /etc/systemd/system/cv_website.service

#To start the daemon run
systemctl start cv_website.service

#To start at boot
systemctl enable cv_website.service

#To debug
# journalctl --unit cv_website.service --follow

# source:
# https://unix.stackexchange.com/questions/426862/proper-way-to-run-shell-script-as-a-daemon
