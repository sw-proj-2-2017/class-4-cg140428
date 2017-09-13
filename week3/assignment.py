#2017.09.13
#20171661 이다은
#성적표 dictionary

import pickle

dbfilename = 'test3_4.dat'


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
        #print(scdb)
        for p in scdb:
            ''' 
            {'Age': '18', 'Name': 'Lee', 'Score': '91'}
            위는 예시이다.
            
            Age 와 Score는 Int값으로 처리해야함.
            
            현재 Age 의 값은 '18' -> 18
            
            '''
            p['Age'] = int(p['Age'])
            p['Score'] = int(p['Score'])
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb



# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while (True):
        #print(scdb)
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ") # inputstr 값으로 공백을 기준으로 하여 잘라 배열 parse에 저장
        #add 명령
        if parse[0] == 'add':
            record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]} #두번째 단어 -> Name의 value, 세번째 -> Age의 value, 네번째 -> Score의 value로 지정하여 dictionary record로 저장
            scdb += [record]
            for p in scdb:
                p['Age'] = int(p['Age']) #문자형인 Age의 value을 int형으로 변환해준다
                p['Score'] = int(p['Score'])
        #del 명령 추가
        elif parse[0] == 'del':
            try:
                scdb_copy = scdb[:] #slice
                for p in scdb_copy:
                    if p['Name'] == parse[1]: #p번째 딕션어리의 Name의 value가 입력 값의 두번째 마디와 같으면
                        scdb.remove(p) #p번째 딕션어리를 삭제한다.
                #break
            except IndexError:
                continue
        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1] # 단어가 하나일경우 true:'Name' false: 두번째 단어
            showScoreDB(scdb, sortKey)
        #find 명령 추가
        elif parse[0] == 'find':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        for i in sorted(p):
                            print(i + "=" + p[i], end=' ')
                        print()
            except IndexError:
                continue
        #inc 명령 추가
        elif parse[0] == 'inc':
            try:
                amount = int(parse[2])
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] = int(p['Score'])
                        p['Score'] = p['Score'] + amount
                        # A += 1   ===   A = A + 1
                        # 1 + 1 = 2 / '1' + '1' = 11
                        # '1' + 1 = ? error
                        # 스트링에서 int로 변환 후 연산하기.
            except IndexError:
                continue
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            # '1' + 1 = ? error
            p[attr] = str(p[attr])
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

