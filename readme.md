
# this code is running on tyryshkin.com

## installation  
```
git clone https://github.com/slavanorm/cv_website.git
sudo apt install apache2 python3
sudo service apache2 start
```  
## auto-update  
this can auto-update website contents once you pushed update to git  
you can enable it with  
```
sh cv_website/bash/install.sh
```  
## logging  
update of git contents logs to ../cv_logs  
you can disable it in bash/cv_daemon.sh
