import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import ImageProc

class Myapp(QMainWindow):

    def __init__(self,parent=None):
        super(Myapp,self).__init__(parent)
        self.date = QDate.currentDate()
        self.initUI()
        self.fileopenwidget = FileopenWidget(self)
        self.setCentralWidget(self.fileopenwidget)

    def initUI(self):
        self.setWindowTitle("점자 번역 계산기")
        self.resize(400,500)
        self.center()

        QToolTip.setFont(QFont('SansSerif', 8))
        self.setToolTip('이 프로그램은 이미지처리를 통한 점자 번역 계산기입니다')
        
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
    
    def center(self):
        windowsize = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        windowsize.moveCenter(cp)
        self.move(windowsize.topLeft())

class FileopenWidget(QWidget):
    
    def __init__(self, parent):        
        super(FileopenWidget, self).__init__(parent)
        self.imagepath = None

        self.pushButton = QPushButton("파일 열기")
        self.pushButton.setFont(QFont("Arial",15,QFont.DemiBold))
        self.pushButton.clicked.connect(self.pushButtonClicked)
        
        self.transButton = QPushButton("계산하기")
        self.transButton.setFont(QFont("Arial",10, QFont.Bold))
        self.transButton.clicked.connect(self.transbuttonClicked)
        
        
        self.label = QLabel("점자 이미지를 불러오세요",self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("border-radius: 10px;border: 1px solid black;")
        self.label.setFont(QFont("Arial",20,QFont.Black))
        
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.transButton)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.imagepath = fname[0]
        pixmap = QPixmap(self.imagepath)
        
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(),pixmap.height())
    
    def transbuttonClicked(self):
        # 원본 이미지의 경로를 받아옴
        imgProc = ImageProc.ImgProc(self.imagepath) 

        imgProc.setImg()                # 경로에서 이미지를 세팅
        imgProc.createPredictDir()      # 예측 가능한 이미지를 위한 디렉토리 생성

        imgProc.cutting()       # 원본 이미지를 예측 가능한 이미지로 분할
                                # 위에서 만든 디렉토리에 저장됨

        imgProc.checkOrigin()   # 원본 이미지 확인
        imgProc.checkPredict(0) # 예측 가능한 이미지들 확인, index번째 이미지 확인, index가 -1이면 모두 확인
        print(imgProc)          # 객체 정보 표시

        imgProc.removePredictDir()      #예측 가능한 이미지를 위한 디렉토리 삭제

class TranslationWidget(QWidget):
    
    def __init__(self, parent):        
        super(TranslationWidget, self).__init__(parent)


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    ex.show()
    sys.exit(app.exec_())