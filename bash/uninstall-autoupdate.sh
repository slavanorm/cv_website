sname='cv_website.service'
systemctl stop $sname
systemctl disable $sname
rm /etc/systemd/system/$sname
systemctl daemon-reload
