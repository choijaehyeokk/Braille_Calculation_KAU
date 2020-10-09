import cv2 as cv
import numpy as np

def cutting(imgPath):
    img = cv.imread(imgPath,cv.IMREAD_UNCHANGED)
    if(img is None):
        return
    size = np.size(img)
    shape = np.shape(img)

    img_cp = np.copy(img)

    braile_letters = list()
    for i in range(1,shape[1]//shape[0]+1):
        cv.line(img_cp,(shape[0]*i,0),(shape[0]*i,shape[0]),(0,0,0),3)
        braile_letters.append(img[:,shape[0]*(i-1):shape[0]*i])
    
    return braile_letters

if __name__ == "__main__":
    filename = input("파일 입력: ")
    print(filename)

    img = cv.imread("./"+ filename +".png")
    cv.imshow("testing",img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    braile_letters = cutting("./"+ filename +".png")
    for letter in braile_letters:
        cv.imshow("result",letter)
        cv.waitKey(0)
        cv.destroyAllWindows()
