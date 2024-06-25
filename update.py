import pyautogui
List = "sudo apt update"
for execute in List:
    pyautogui.press(execute)
pyautogui.press('enter')
