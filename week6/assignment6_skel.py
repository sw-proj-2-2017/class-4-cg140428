import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):
        name = QLabel("Name: ")
        age = QLabel("Age: ")
        score = QLabel("Score: ")
        amount = QLabel("Amount: ")
        key = QLabel("Key: ")
        result = QLabel("Result: ")

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.keyCombo = QComboBox()
        self.keyCombo.addItems(["Name", "Age", "Score"])
        self.resultTextEdit = QTextEdit()

        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        findButton = QPushButton("Find")
        incButton = QPushButton("Inc")
        showButton = QPushButton("show")

        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()

        hbox.addWidget(name)
        hbox.addWidget(self.nameEdit)
        hbox.addWidget(age)
        hbox.addWidget(self.ageEdit)
        hbox.addWidget(score)
        hbox.addWidget(self.scoreEdit)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(key)
        hbox2.addWidget(self.keyCombo)
        hbox3.addWidget(addButton)
        hbox3.addWidget(delButton)
        hbox3.addWidget(findButton)
        hbox3.addWidget(incButton)
        hbox3.addWidget(showButton)
        hbox4.addWidget(result)
        hbox5.addWidget(self.resultTextEdit)

        vbox = QVBoxLayout()

        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)

        addButton.clicked.connect(self.addDB)
        delButton.clicked.connect(self.delDB)
        findButton.clicked.connect(self.findDB)
        incButton.clicked.connect(self.incDB)
        showButton.clicked.connect(self.showDB)


        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()



    def addDB(self):
        if self.nameEdit.text() and self.ageEdit.text() and self.scoreEdit.text():
            try:
                record = {'Name': self.nameEdit.text(), 'Age': int(self.ageEdit.text()), 'Score': int(self.scoreEdit.text())} #두번째 단어 -> Name의 value, 세번째 -> Age의 value, 네번째 -> Score의 value로 지정하여 dictionary record로 저장
                self.scoredb += [record]
                self.showScoreDB()
            except (ValueError, IndexError):
                print("add Name Age Score순으로 입력해주세요.")


    def delDB(self):
        if self.nameEdit.text():
            try:
                scdb_copy = self.scoredb[:] #slice
                for p in scdb_copy:
                    if p['Name'] == self.nameEdit.text(): #p번째 딕션어리의 Name의 value가 입력 값의 두번째 마디와 같으면
                        self.scoredb.remove(p) #p번째 딕션어리를 삭제한다.
                #break
                self.showScoreDB()
            except (ValueError, IndexError):
                print("del Name순으로 입력해주세요.")


    def findDB(self):
        if self.nameEdit.text():
            try:
                a = ""
                for p in self.scoredb:
                    if p['Name'] == self.nameEdit.text():
                        for attr in p:
                            a += attr + "=" + str(p[attr]) + "\t"  # 주어진 name의 정보 출력
                        a += "\n"
                self.resultTextEdit.setText(a)
            except:
                print("find Name순으로 입력해주세요.")


    def incDB(self):
        try:
            amount = int(self.amountEdit.text())
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    p['Score'] = int(p['Score'])
                    p['Score'] = p['Score'] + amount
                    # A += 1   ===   A = A + 1
                    # 1 + 1 = 2 / '1' + '1' = 11
                    # '1' + 1 = ? error
                    # 스트링에서 int로 변환 후 연산하기.
            self.showScoreDB()
        except (IndexError, ValueError):
            print("inc Name Score순으로 입력해주세요.")


    def showDB(self):
        self.showScoreDB(self.keyCombo.currentText())

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, keyname="Name"):
        a = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                p[attr] = str(p[attr])
                a += attr + "=" + p[attr] + "\t"
            a += "\n"
        self.resultTextEdit.setText(a)
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





