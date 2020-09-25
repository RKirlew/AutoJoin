
import pyautogui
from time import sleep

accept=None
f= None
r= None
c=None
chooseNum=0
l=None
lockIn=None

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
def checkAccept():
    global accept
    global lockIn
    while accept is None:
        accept=pyautogui.locateCenterOnScreen('button.png', grayscale=False,confidence=0.5)
        if accept:
                     pyautogui.moveTo(accept[0],accept[1])
                     pyautogui.click()
                     pyautogui.moveTo(accept[0],accept[1]-150)
                     pyautogui.click()
                     return True
def banChamp():
    detectNum=0
    b= None
    banThis=None
    while b is None:
       

        b=pyautogui.locateCenterOnScreen('bans.png',grayscale=False,confidence=0.5)
        if b:
            try:
                print(ban)
                test=pyautogui.locateCenterOnScreen(ban,grayscale=False,confidence=0.5)
                pyautogui.moveTo(test[0],test[1])
                pyautogui.click()
                detectNum+=1
                if banThis is None:
                    banThis=pyautogui.locateCenterOnScreen("ban.png",grayscale=False,confidence=0.5)
                    pyautogui.moveTo(banThis[0],banThis[1])
                    pyautogui.click()
            except:
                pyautogui.scroll(-115)
                
def draft():
    lockin=None
    global img
    print(img+" is the global variable")
    global ban
    global lockIn
    global b
    choose=None
    b= None
    banThis=None
    while b is None:
       

        b=pyautogui.locateCenterOnScreen('bans.png',grayscale=False,confidence=0.5)
        if b:
            try:
                print(ban)
                test=pyautogui.locateCenterOnScreen(ban,grayscale=False,confidence=0.5)
                pyautogui.moveTo(test[0],test[1])
                pyautogui.click()
               
                if banThis is None:
                    banThis=pyautogui.locateCenterOnScreen("ban.png",grayscale=False,confidence=0.5)
                    pyautogui.moveTo(banThis[0],banThis[1])
                    pyautogui.click()
                    
               
            except:
               
                pyautogui.scroll(-115)
    if banThis is not None:            
        while choose is None:
                choose=pyautogui.locateCenterOnScreen("choose.png",grayscale=False,confidence=0.5)
                if choose:
                    try:
                        print(img+" was chosen")
                        c=pyautogui.locateCenterOnScreen(img,grayscale=False,confidence=0.5)
                        pyautogui.moveTo(c[0],c[1])
                        pyautogui.click()
                        c=1
                        if lockin is None:
                            lockin=pyautogui.locateCenterOnScreen("lock-in.png",grayscale=False,confidence=0.5)
                            pyautogui.moveTo(lockin[0],lockin[1])
                            pyautogui.click()
                            lockIn=1
                            chooseNum+=1
                            if chooseNum>1:
                                img=secondary
                    except:
                        pyautogui.scroll(-115)


               
                    
if mode == 'd':
    #checkAccept()
    while lockIn is None:
        checkAccept()
        draft()

if mode =='b':
            while c is None:
                while l is None:
                    l=pyautogui.locateCenterOnScreen("choose.png",grayscale=False,confidence=0.5)
                if l:
                    try:
                        print(img+" was chosen")
                        c=pyautogui.locateCenterOnScreen(img,grayscale=False,confidence=0.5)
                        pyautogui.moveTo(c[0],c[1])
                        pyautogui.click()
                        c=1
                        if lockin is None:
                            lockin=pyautogui.locateCenterOnScreen("lock-in.png",grayscale=False,confidence=0.5)
                            pyautogui.moveTo(lockin[0],lockin[1])
                            pyautogui.click()
                    except:
                        pyautogui.scroll(-115)
                   
        
    
   
        
       
print(c)
