from cv2 import cv2 as cv
import numpy as np
import os

class ImgProc:
    ''' 
        Image processing for predict
    '''

    def __init__(self,imgPath):
        '''
        imgPath: 이미지 경로
        width: 이미지 넓이
        height: 이미지 높이
        length: 잘려질 이미지 수
        originImg: 이미지 경로속 이미지의 배열
        predictDir: 예측 디렉토리 경로
        dividedImg: 잘려진 이미지의 배열들을 원소로 갖는 list
        callNum: savePiece가 호출된 횟수를 기록
        '''
        self.imgPath = imgPath
        self.width = 0
        self.height = 0
        self.length = 0
        self.originImg = None
        self.predictDir = ""
        self.dividedImg = None

        self.callNum = 0
        
    def delImg(self, path):
        if os.path.isfile(path):
            os.remove(path)

    def setImg(self):
        '''
            imgPath의 경로에 있는 이미지를 가져와 객체에 저장한다.
        '''
        self.originImg = cv.imread(self.imgPath,cv.IMREAD_UNCHANGED)
        shape = np.shape(self.originImg)
        self.height = shape[0]
        self.width = shape[1]
        self.length = shape[1]//shape[0]

    def createPredictDir(self):
        '''
            예측을 위한 디렉토리를 만들어 predictDir에 저장한다.
        '''
        path = "./assets/predict"
        try:
            try:
                os.mkdir(path)
            except:
                pass
            os.mkdir(path+"/images")
            print('예측을 위한 디렉토리 생성')
        except:
            print('이미 디렉토리가 존재합니다.')
            pass
        self.predictDir = path

    def removePredictDir(self):
        '''
            예측을 위한 디렉토리와 그 안에 있는 모든 파일과 디렉토리를 삭제한다.
        '''
        try:
            for root, dirs, files in os.walk(self.predictDir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(self.predictDir)
            self.predictDir = ""
            self.dividedImg = None
            print("예측을 위한 디렉토리 삭제 완료")
        except:
            print('삭제에 실패')

    def checkPredictDir(self):
        '''
            예측을 위한 디렉토리가 있는지 확인한다.
        '''
        if self.predictDir == "":
            return False
        else:
            return True

    def cutting(self):
        '''
            예측을 위해 원본 이미지를 잘라 예측 가능한 이미지로 만든다.
        '''
        try:
            self.dividedImg = list()
            for i in range(0,self.length):
                #cv.imwrite(self.predictDir + "/images/" + str(i) + ".png", self.originImg[:,self.height*i:self.height*(i+1)])
                self.dividedImg.append(self.originImg[:,self.height*i:self.height*(i+1)])
        except:
            print("예외 발생")
    
    def savePiece(self):
        if not self.checkPredictDir():
            print("예측을 위한 디렉토리가 없음")
            return
        elif self.dividedImg is None:
            print("잘려진 이미지 없음")
            return
        elif self.callNum >= len(self.dividedImg):
            print("index를 초과했습니다.")
            return
        cv.imwrite(self.predictDir + "/images/" + str(self.callNum) + ".png", self.dividedImg[self.callNum])
        self.callNum += 1

    def checkOrigin(self):
        '''
            원본이미지를 출력한다.
        '''
        if self.originImg is not None:
            cv.imshow("Origin", self.originImg)
            cv.waitKey(0)
            cv.destroyAllWindows()
        else:
            print("셋팅된 이미지가 없습니다.")

    def checkPredict(self,index):
        '''
            예측 가능한 이미지를 출력한다.
            index: 몇번째 예측 가능한 이미지를 출력할지 정하는 매개변수,
                    -1일 경우 모든 예측 가능한 이미지를 출력한다.
        '''
        try:
            if index == -1:
                for i in range(len(self.dividedImg)):
                    cv.imshow("Predict", self.dividedImg[i])
                    cv.waitKey(0)
                    cv.destroyAllWindows()
            else:
                cv.imshow("Predict", self.dividedImg[index])
                cv.waitKey(0)
                cv.destroyAllWindows()
        except:
            print("셋팅된 이미지가 없습니다.")

    def __str__(self):
        '''
            현재 객체 정보를 출력한다.
        '''
        text = "imgPath: " + str(self.imgPath) + "\n" +\
               "width: " + str(self.width) + "\n" +\
               "height: " + str(self.height) + "\n" +\
               "length: " + str(self.length) + "\n" +\
               "originImg: " + str(self.originImg) + "\n" + \
               "predictDir: " + self.predictDir + "\n" + \
               "dividedImg: " + str(self.dividedImg) + "\n"
        return text

if __name__ == "__main__":
    imgProc = ImgProc("../4IRSWContest/assets/image/test/(3x2)+3(div)1-2+9x6+3.png")

    imgProc.setImg()
    imgProc.createPredictDir()

    imgProc.cutting()
    for i in range(imgProc.length):
        imgProc.savePiece()
        imgProc.delImg("./assets/predict/images/"+str(i)+".png")

    imgProc.checkOrigin()

    imgProc.checkPredict(0)

    print(imgProc)

    #imgProc.removePredictDir()
