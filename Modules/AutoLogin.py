import time
from Engine.GUI import *
from Core.GetAccountNamePosition import GetAccountNamePosition

get_login_location = False
EnabledAutoLogin = False
bool_login = False

Login = [0, 0]
AccountName = [0, 0]

username_value = ''
passwd_value = ''


class AutoLogin:
    def __init__(self, root):
        self.AutoLogin = GUI('AutoLogin', 'Module: Auto Login')
        self.AutoLogin.DefaultWindow('AutoLogin', [339, 540], [1.2, 2.29])

        def SetAutoLogin():
            global EnabledAutoLogin
            if not EnabledAutoLogin:
                EnabledAutoLogin = True
                print("AutoLogin: ON")
                ButtonEnabled.configure(text='AutoLogin: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
                CheckingButtons()
                ScanAutoLogin()
            else:
                EnabledAutoLogin = False
                print("AutoLogin: OFF")
                CheckingButtons()
                ButtonEnabled.configure(text='AutoLogin: OFF', relief=RAISED, bg=rgb((127, 17, 8)))

        def ScanAutoLogin():
            global EnabledAutoLogin
            if EnabledAutoLogin:
                AccountName = GetAccountNamePosition()
                if AccountName[0] and AccountName[1] != 0:
                    print("You Are Offline... Trying To Login")
                    login = pyautogui.locateOnScreen('images/TibiaSettings/Login.png', grayscale=True, confidence=0.8)
                    print("Your Login location is:", login)
                    Login[0], Login[1] = pyautogui.center(login)
                    global username_value
                    username_value = username.get()
                    global passwd_value
                    passwd_value = passwd.get()
                    time.sleep(1)
                    global pass_mouse_position
                    if Login is not None:
                        pass_mouse_position = pyautogui.position()
                        pyautogui.click(x=AccountName[0], y=AccountName[1])
                        pyautogui.write(username_value, interval=0.15)
                        pyautogui.press('tab')
                        pyautogui.write(passwd_value, interval=0.15)
                        pyautogui.click(Login[0], Login[1])
                        time.sleep(2)
                        pyautogui.press('enter')
                        pyautogui.moveTo(pass_mouse_position)
                        AccountName2 = pyautogui.locateOnScreen('images/TibiaSettings/AccountName.png',
                                                                grayscale=True,
                                                                confidence=0.8)
                        if AccountName2 is not None:
                            print("Error To Login !!!!")
                        else:
                            print("You Are Logged")
                    else:
                        print("Error To Locate Login Button!")
                else:
                    print("You Are Online...")

            if EnabledAutoLogin:
                root.after(3000, ScanAutoLogin)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()
        TextEntryUsername = tk.StringVar()
        TextEntryYPasswd = tk.StringVar()

        self.AutoLogin.addButton('Ok', self.AutoLogin.destroyWindow, [84, 29], [130, 504])

        global EnabledAutoLogin
        if not EnabledAutoLogin:
            ButtonEnabled = self.AutoLogin.addButton('AutoLogin: OFF', SetAutoLogin, [328, 29], [12, 469])
        else:
            ButtonEnabled = self.AutoLogin.addButton('AutoLogin: ON', SetAutoLogin, [328, 29], [12, 469])

        ButtonPrint = self.AutoLogin.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AutoLogin.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        username_label = self.AutoLogin.addLabel('Username', [130, 16, 6], [69, 84])

        username = self.AutoLogin.addEntry([149, 86], TextEntryUsername, 10)
        global username_value
        username_value = username.get()

        passwd_label = self.AutoLogin.addLabel('Password', [130, 16, 6], [69, 124])

        passwd = self.AutoLogin.addEntry([149, 126], TextEntryYPasswd, 10)
        global passwd_value
        passwd_value = passwd.get()

        def CheckingButtons():
            if EnabledAutoLogin:
                username_label.configure(state='disabled')
                passwd_label.configure(state='disabled')
                username.configure(state='disabled')
                passwd.configure(state='disabled')
            else:
                username_label.configure(state='normal')
                passwd_label.configure(state='normal')
                username.configure(state='normal')
                passwd.configure(state='normal')

        CheckingButtons()

        self.AutoLogin.loop()

