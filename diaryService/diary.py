from util import util_time
from diaryService import config as diary_config
import config as root_config
from util.dumy import existMembers
import session
import json
import os


def run():
    flag = True
    while flag:
        if session.getSignInedMemberId() == '':
            menuNum = int(input('1.WRITE 2. READ 3. UPDATE 4. DELETE 99. END_SERVICE').strip())

        if menuNum == diary_config.WRITE:
            pass
        elif menuNum == diary_config.READ:
            pass
        elif menuNum == diary_config.UPDATE:
            pass
        elif menuNum == diary_config.DELETE:
            pass
        elif menuNum == diary_config.END_SERVICE:
            flag = False


def init_database():
    global members
    global dbFile
    dbFile = ''

    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    print(f'BASE_PATH: {BASE_PATH}')

    ROOT_DIR = os.path.dirname(BASE_PATH)
    print(f'ROOT_DIR: {ROOT_DIR}')

    dbFile = os.path.join(ROOT_DIR, 'db', 'diary.json')
    print(f'dbFile: {dbFile}')

    if not os.path.exists(dbFile):
        save_members(existMembers)
    else:
        members = load_members()


def save_members(members):  #위에 코딩하려는 내용을 밑으로 뻈다.
    with open(dbFile, 'w', encoding='utf-8') as f:
            json.dump(members, f, ensure_ascii=False, indent=4) #기존 내용을 지우고 새로  적는 내용으로 덮어씌운다.

def load_members():
    with open(dbFile, 'r', encoding='utf-8') as f:
        return json.load(f)
        #로드는 내용을 파이썬에 맞게 가져오는 것

if __name__ == '__main__':
    init_database()
    run()