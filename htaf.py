import pyautogui
List = "sudo apt install maven; sudo apt install jetbrains-aqua; mvn -V; jetbrains-aqua -V;"
for execute in List:
    pyautogui.press(execute)
pyautogui.press('enter')
