import pyautogui
List = "sudo apt install postgresql; ssudo systemctl start postgresql.service; sudo systemctl status postgresql.service; sudo -i -u postgres psql; CREATE USER 'root' WITH ENCRYPTED PASSWORD '123'; ALTER USER root WITH SUPERUSER; \du; \q; psql -V"
for execute in List:
    pyautogui.press(execute)
pyautogui.press('enter')
