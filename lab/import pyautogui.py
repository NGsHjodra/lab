import pyautogui
import time
import cv2
import webbrowser
import win32api, win32con

def click (position) :
    x = int(position[0] + position[2]/2)
    y = int(position[1] + position[3]/2)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def Oneclick(filename):
    while True :
        position = pyautogui.locateOnScreen(filename, confidence=0.9)
        if position is not None:
            click(position)
            print(filename + " clicked")
            break
    
def Multipleclick(filename):
    while True :
        position = pyautogui.locateOnScreen(filename, confidence=0.9)
        
        if position is None :
            pyautogui.scroll(-500) 
            print("srcoll")
            position = pyautogui.locateOnScreen(filename, confidence=0.9)
        
            if position is None:
                print("pass") 
                break
            
        click(position)
        print(filename + " clicked")
        
def InitTask(filename):
     while True :
        position = pyautogui.locateOnScreen(filename, confidence=0.9)
        if position is not None:
            break

webbrowser.open('https://netcovid.sut.ac.th/auth/', new=1)
#pyautogui.FAILSAFE = True

Oneclick('click1.PNG')

Oneclick('click2.PNG') 
pyautogui.write('6230549')

Oneclick('click3.PNG') 
pyautogui.write('1109')

pyautogui.press('enter')

Oneclick('clickNo.PNG')

Multipleclick('clickNo2.PNG')

Oneclick('save.PNG')

Oneclick('save2.PNG')