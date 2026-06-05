import config

def main():
    flag = True
    while flag:
        menuNum = int(input('1.MEMBER 2.diary 99. system_out ')).strip()
        if menuNum == config.MEMBER_SERVICE :
            pass
        elif menuNum == config.DIARY_SERVICE:
            pass
        
        elif menuNum == config.SYSTEM_OUT:
            flag = False


    if __name__ == '__main__':
        main()