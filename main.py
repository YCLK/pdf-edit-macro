import pyautogui
import pyperclip
import time
import os

# 687 233
# 1528 233

# 안내
print('Auto PDF Edit Macro (Ver 1.0)    제작: YCLK')
time.sleep(3)

allPage = int(input('전체 PDF 페이지를 입력해 주세요: '))

# 시작 안내
time_cnt = 3

while time_cnt:
    print(str(time_cnt) + '초 후에 매크로가 작동됩니다.')
    time_cnt -= 1
    time.sleep(1)
os.system('cls')

# num변수 선언
num = 0

while num < allPage:
    num += 1
    pyautogui.moveTo(687, 233, duration=0.3)
    pyautogui.dragTo(1528, 233, duration=0.3)
    pyautogui.press('enter')
    pyautogui.press('right')