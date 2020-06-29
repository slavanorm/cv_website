
# code running tyryshkin.com

## usage
1 fork  
2 install  
3 fill your cv.txt with text or HTML  
4 parse cv to html: python3 cv_website/main.py  
5 that's it!

## installation  
```
git clone https://github.com/slavanorm/cv_website.git \
sudo apt install apache2 python3 \
sudo service apache2 start
```  
## auto-update content on git push  
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
