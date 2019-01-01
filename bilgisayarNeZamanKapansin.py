import pyautogui
import os
time = pyautogui.prompt(text="Lütfen kaç saniye içerisinde kapanacağını giriniz",title="Hasario")
os.system("shutdown /s /t %s " % time)