import pyautogui
List = "sudo apt install code; sudo apt install nodejs; sudo apt install npm; sudo snap install docker; sudo apt install git; code -V; nodejs -V; npm -V; docker -V; git -V"
for execute in List:
    pyautogui.press(execute)
pyautogui.press('enter')
