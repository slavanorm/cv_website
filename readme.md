
# code running tyryshkin.com

## usage
1 fork  
2 install  
3 fill your cv.txt with text or HTML  
4 update site: py cv_website/main.py  
5 that's it!

## installation  
```
git clone -b release/0.1 https://github.com/slavanorm/cv_website.git
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
