if __name__ == "__main__":
    try:
        import os
        from pathlib import Path
        from colorama import Fore
        if os.path.isfile("zAdminAccount.txt"): pass
    except Exception as e:
        print(e)
        os.system("pip install pathlib")
        os.system("pip install colorama")
        input("알 수 없는 오류가 발생 하였습니다.")
    else:
        check = Path("zAdminAccount.txt").read_text()
        if ":" in check:
            acc = check.split(":")[0]
            pw = check.split(":")[1]

            os.system("cls")

            print(f"""{Fore.BLUE}
            
            ███████ ██████      ███████ ████████  ██████  ██████  ██    ██ ███████ ██████   █████  ███    ███ 
            ██      ██   ██     ██         ██    ██    ██ ██   ██  ██  ██  ██      ██   ██ ██   ██ ████  ████ 
            █████   ██████      ███████    ██    ██    ██ ██████    ████   ███████ ██████  ███████ ██ ████ ██ 
            ██      ██   ██          ██    ██    ██    ██ ██   ██    ██         ██ ██      ██   ██ ██  ██  ██ 
            ██      ██████      ███████    ██     ██████  ██   ██    ██    ███████ ██      ██   ██ ██      ██ 
                                                                                                  
            {Fore.RESET}                                                                                    
            {Fore.CYAN} 
            Github : https://github.com/WhiteHole00
            Telegram : https://t.me/whitehole0906
            {Fore.RESET}
                                                                {Fore.GREEN}By WhiteHole{Fore.RESET}

            {Fore.LIGHTMAGENTA_EX}
            ┌─  FaceBook Story Spammer ─────────────────────────────────────────┐
            │  [1] RunSpam                                                      │
            │  [2] Quit                                                         │
            └───────────────────────────────────────────────────────────────────┘
            {Fore.RESET}
            """)
            cho = input('''
            │
            └─> ''')

            if cho == "1":
                msg = input("도배할 메세지를 입력 해 주세요 >> ")
                cnt = int(input("도배할 횟수를 입력 해 주세요 >> "))
                from StorySpam.StorySpammer import isStorySpam
                isGoSpam = isStorySpam(cnt,msg,acc,pw)

                if isGoSpam == True:
                    print(f"""{Fore.BLUE}
                ███████ ██████      ███████ ████████  ██████  ██████  ██    ██ ███████ ██████   █████  ███    ███ 
                ██      ██   ██     ██         ██    ██    ██ ██   ██  ██  ██  ██      ██   ██ ██   ██ ████  ████ 
                █████   ██████      ███████    ██    ██    ██ ██████    ████   ███████ ██████  ███████ ██ ████ ██ 
                ██      ██   ██          ██    ██    ██    ██ ██   ██    ██         ██ ██      ██   ██ ██  ██  ██ 
                ██      ██████      ███████    ██     ██████  ██   ██    ██    ███████ ██      ██   ██ ██      ██ 
                                                                                                    
                {Fore.RESET}                                                                                    
                {Fore.CYAN} 
                Github : https://github.com/WhiteHole00
                Telegram : https://t.me/whitehole0906
                {Fore.RESET}
                                                                    {Fore.GREEN}By WhiteHole{Fore.RESET}       
                    """)
                    print(f"{Fore.GREEN}[SUCCESS] : FINISHED UR STORY SPAM IN FACEBOOK {Fore.RESET}")
                    input("PLZ ENTER TO QUIT")
                else:
                    print(f"{Fore.RED}[FAIL] : UNKNOWN ERROR! {Fore.RESET}")
                    input("PLZ ENTER TO QUIT")
            elif cho == "2":
                input("PLZ ENTER TO QUIT")
            else:
                print(f"{Fore.RED}[FAIL] : INVAILD NUMBER 3 SECONDS LATER U WILL GO MENU {Fore.RESET}")
        else:
            input("계정 형식이 잘못 되었습니다.")   
