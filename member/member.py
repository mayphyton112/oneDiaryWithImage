from util import util_time
from member import config as member_config
import config as root_config
import session
from util import dumy
import json

members = dumy
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
        'mDegdate': util_time.getCurrentDateIime(),
        'mModdate': util_time.getCurrentDateIime()
    }
    
    members[mId] = newMember
    #members 딕셔너리에 키는 mId, 벨류는 newMember를 저장한다.
    print('MEMBER SIGN_UP SUCCESS')


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
            pass
        elif menuNum == member_config.MODIFY:
            pass
        elif menuNum == member_config.DELETE:
            pass
        elif menuNum == member_config.SIGN_OUT:
            pass
        elif menuNum == member_config.END_SERVICE:
            flag = False

    


if __name__ == '__main__':
    run()