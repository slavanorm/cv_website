
# this code is running on tyryshkin.com

## installation  
```
git clone https://github.com/slavanorm/cv_website.git
sudo apt install apache2 python3
sudo service apache2 start
```  
## auto-update on git push  
enable:  
```
sh cv_website/bash/install-autoupdate.sh
```  
disable:  
```
sh cv_website/bash/uninstall-autoupdate.sh
```  
## logging  
```
journalctl --unit cv_website.service --follow
```
