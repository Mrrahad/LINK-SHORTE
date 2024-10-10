import sys
import time
import pyshorteners
username = "shakil"
password = "1234"

def end():
  shakil = input()
  sys.exit()
  
  
given_username = input("Enter your username:")
if given_username == username:
  print("\033[0;32mCORRECT USERNAME")   
  given_passwrd = input("your password:")
  if given_passwrd ==password:  
    print("\033[0;32mCYBER SECURITY 67JOIN")    

else:
 ("wrong username")
 time.sleep(2)
 print("\033[0;31mpress enter to exit")
 end()
 
  #else:
 print("/033[0;35wrong password")    
 time.sleep(2)
 print("\033[0;31mpress enter to exit")
 end()

import sys 
import time 
def animated (text):
  for x in text:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.005)

logo  = ( """

 \033[0;31m ______   __    __   ______   __    __  ______  __       
 /      \ /  |  /  | /      \ /  |  /  |/      |/  |      
/$$$$$$  |$$ |  $$ |/$$$$$$  |$$ | /$$/ $$$$$$/ $$ |      
$$ \__$$/ $$ |__$$ |$$ |__$$ |$$ |/$$/    $$ |  $$ |      
$$      \ $$    $$ |$$    $$ |$$  $$<     $$ |  $$ |      
 $$$$$$  |$$$$$$$$ |$$$$$$$$ |$$$$$  \    $$ |  $$ |      
/  \__$$ |$$ |  $$ |$$ |  $$ |$$ |$$  \  _$$ |_ $$ |_____ 
$$    $$/ $$ |  $$ |$$ |  $$ |$$ | $$  |/ $$   |$$       |
 $$$$$$/  $$/   $$/ $$/   $$/ $$/   $$/ $$$$$$/ $$$$$$$$/ 
                                                          
                                                          
                                                          
                                                          
""")
animated(logo)

link = input("enter your link here :")
s = pyshorteners.Shortener()
provite = s.tinyurl.short(link)
  
print(f"your short link is : {provite}")