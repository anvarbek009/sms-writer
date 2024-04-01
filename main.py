import time
import pyautogui
a="Hello this hack message"
b=10
print("Boshlandi")
while b!=0:
    time.sleep(1)
    print(f"{b}s qoldi")
    b-=1
print("start")
for i in range(10):
    pyautogui.typewrite(a+"\n")
    print(i,"jo'natildi")

