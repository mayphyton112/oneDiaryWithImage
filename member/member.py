from util import util_time
from member import config as member_config
import config as root_config
from util.dumy import existMembers
import session
import json
import os


members = {}
def sign_up():
    mId = input('새 id 입력: ')
    if mId in members:
        print('이미 사용중인 ID')
        return
    mPw = input('새 pw입력: ')
    mMail = input('새 mail입력: ')
    mPhone = input('새 phone입력: ')

    newMember = {
        'mId': mId,
        'mPw': mPw,
        'mMail': mMail,
        'mPhone': mPhone,
        'mRegdate': util_time.getCurrentDateTime(),
        'mModdate': util_time.getCurrentDateTime()
    }
    
    members[mId] = newMember
    save_members(members)
    #members 딕셔너리에 키는 mId, 벨류는 newMember를 저장한다.
    print('MEMBER SIGN_UP SUCCESS')

    if root_config.DEV_MOD:
        print(f'load_members(): {load_members()}')

def sign_in():
    mId = input('ID입력: ').strip()
    mPw = input('PW 입력: ').strip()

    if mId in members and members[mId]['mPw'] == mPw:
        print('MEMBER SIGN_IN SUCCESS')
        session.setSignInedMemberId(mId)

        if root_config.DEV_MOD:
            print(f'session.signInedMemberId: {session.signInedMemberId}')
        return
    print('MEMBER SIGN_IN FAIL')

def modify():
    mPw = input('새 pw 입력: ').strip()
    mMail = input('새 mail 입력: ').strip()
    mPhone = input('새 phone 입력: ').strip()

    members = load_members()
    memberForModify = members[session.getSignInedMemberId()]

    memberForModify['mPw'] = mPw
    memberForModify['mMail'] = mMail
    memberForModify['mPhone'] = mPhone
    memberForModify['mModdate'] = util_time.getCurrentDateTime()


    save_members(members)
    print('MODIFY SUCCESS')

    if root_config.DEV_MOD:
        print(f'self.load_members(): {load_members()}')

def delete():
    confirm = input('정말 탈퇴하겠습니까? [Y] or [N]')
    if confirm == 'Y':
        del members[session.getSignInedMemberId()]
        save_members(members)
        session.setSignInedMemberId()
        print('DELETE SUCCESS')
def sign_out():
    session.setSignInedMemberId()
    print('SIGN_OUT SUCCESS')

def run():
    flag = True
    while flag:
        if session.getSignInedMemberId() == '':
            menuNum = int(input('1. SIGN_UP 2. SIGN_IN 99. END_SERVICE').strip())
        else:
            menuNum = int(input('3. MODIFY 4. DELETE 5. SIGN_OUT 99. END_SERVICE').strip())
        
        if menuNum == member_config.SIGN_UP:
            sign_up()
        elif menuNum == member_config.SIGN_IN:
            sign_in()
        elif menuNum == member_config.MODIFY:
            modify()
        elif menuNum == member_config.DELETE:
            delete()
        elif menuNum == member_config.SIGN_OUT:
            sign_out()
        elif menuNum == member_config.END_SERVICE:
            flag = False

def init_database():
    global members
    global dbFile
    dbFile = ''

    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    print(f'BASE_PATH: {BASE_PATH}')

    ROOT_DIR = os.path.dirname(BASE_PATH)
    print(f'ROOT_DIR: {ROOT_DIR}')

    dbFile = os.path.join(ROOT_DIR, 'db', 'members.json')
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