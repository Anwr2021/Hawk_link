#!/usr/bin/env python3
#
# warna
h="\033[32;1m"
b="\033[36;1m"
import requests,os,sys
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

os.system("clear")

os.system("toilet -f future Hawk Hacker | lolcat" )
banner= h+"""
[•]───────────────────────────────────────────[•]
           This tool shortens links
[•]───────────────────────────────────────────[•]  """
print(banner)

def Hawklink():
	 
    print("""{1}{2}{1}
┏━┓╻ ╻┏━┓┏━┓╺┳╸ ╻  ╻┏┓╻╻┏
┗━┓┣━┫┃ ┃┣┳┛ ┃  ┃  ┃┃┗┫┣┻┓
┗━┛╹ ╹┗━┛╹┗╸ ╹  ┗━╸╹╹ ╹╹ ╹
  {0}{1}Hawk link{2} 
""".format(end,bold,cyan))
Hawklink()
url = input("\033[0m\033[1m\033[36m~/URL# \033[0m\033[1m")
tiny = 'http://tinyurl.com/api-create.php?url='+url
info = requests.get(tiny)
print("\033[0m\033[1m\033[36m~/Link# \033[0m\033[1m"+info.text)

