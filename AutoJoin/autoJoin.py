
import pyautogui
from time import sleep

accept=None
f= None
r= None
c=None
l=None
lockin=None

test=None
champ= input("Which champ:")

secondary=input("Which secondary:")
secondary=secondary.lower()
secondary=secondary.strip()

champ=champ.lower()
champ=champ.strip()
ban= input("Which ban:")

ban=ban.lower()
ban=ban.strip()

mode=input("Draft(D) or Blind (B)")
mode=mode.lower()
mode=mode.strip()

if champ=="blitzcrank":
    champ="blitz"
img=champ+".png"
secondary=secondary+".png"

ban=ban+".png"

def draft():
    global ban
    global b
    b= None
    banThis=None
    while b is None:
       

        b=pyautogui.locateCenterOnScreen('bans.png',grayscale=False,confidence=0.5)
        if b:
            try:
                print(ban)
                test=pyautogui.locateOnScreen(ban,grayscale=False,confidence=0.5)
                pyautogui.moveTo(test[0],test[1])
                pyautogui.click()
                sleep(2)
                while banThis is None:
                    banThis=pyautogui.locateCenterOnScreen("ban.png",grayscale=False,confidence=0.5)
                    pyautogui.moveTo(banThis[0],banThis[1])
                    pyautogui.click()
               
            except:
               
                pyautogui.scroll(-125)
            
while True:
    while lockin is None:    
        # This detects the accept button and clicks it
        #TBI: Constant checking of the button in case a match is dropped due to someone not accepting/dodging
        """accept=pyautogui.locateCenterOnScreen('button.png', grayscale=False,confidence=0.5)
        if accept:
                 pyautogui.moveTo(accept[0],accept[1])
                 pyautogui.click()
        else:
            continue
            print("Not found")"""
               
                    
        if mode == 'd':
            draft()
            
        # This bit of code detects the champion chosen by the user and click    
        """   
        while c is None:
            while l is None:
                 # This bit of code detects the "Choose A Champion" banner
                l=pyautogui.locateCenterOnScreen("choose.png",grayscale=False,confidence=0.5)
            if l:
                try:
                    print(img+" was chosen")
                     # This bit of code detects the champion chosen by the user , moves the cursor to it and clicks it
                    c=pyautogui.locateCenterOnScreen(img,grayscale=False,confidence=0.5)
                    pyautogui.moveTo(c[0],c[1])
                    pyautogui.click()
                    c=1
                    if lockin is None:
                         # Lock in button clicking
                        lockin=pyautogui.locateCenterOnScreen("lock-in.png",grayscale=False,confidence=0.5)
                        pyautogui.moveTo(lockin[0],lockin[1])
                        pyautogui.click()
                except:
                    # If the champion isn't found, scroll down
                    pyautogui.scroll(-115)
                    """
        
    
   
        
       
print(c)
