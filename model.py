import os
from keras.models import load_model
from keras_preprocessing.image import ImageDataGenerator
import operator

def getModel():
        return load_model("./BrailleRecogModel.h5")

def getTestGen(newfolder):
        test_datagen = ImageDataGenerator()
        test_generator = test_datagen.flow_from_directory(
                newfolder,
                target_size=(64, 64),
                batch_size=5,
                class_mode='categorical')

class predict_Class():
    result = []
    ans = [0,1,'/','.','=','(','-','*','number','+',')',2,3,4,5,6,7,8,9]
    def Predict(self, model, real):
        my_list = model.predict(real)
        for i in range(len(my_list)):
            temp = max(enumerate(my_list[i]),key=operator.itemgetter((1)))[0]
            self.result.append(self.ans[temp])
        #index,value = max(enumerate(my_list[0]), key=operator.itemgetter(1))
        #self.result.append(self.ans[index])
        #print(f'예측값 : {self.ans[index]}')
        return self.result

    def reset(self):
        self.result = []

def load_image(img_path):
    images_dir = img_path
    datagen = ImageDataGenerator()
    real_generator = datagen.flow_from_directory(images_dir, target_size=(64,64))
    return real_generator

def delImg(path):
    print("파일 확인")
    if os.path.isfile(path):
        print("파일 있음->지움")
        os.remove(path)

def action(path): # 원래는 합쳐진 이미지가 있는 경로 설정
    #그 후 합쳐진 이미지를 자르는 코드 여기
    #자른 이미지를 저장한 경로를 path에 저장
    print(path)
    ls = os.listdir(path+"images/")
    len_files = len(ls)
    print(len_files)
    a = predict_Class()
    a.reset()
    real = load_image(path)
    a.Predict(getModel(), real)

    return a.result

def result_to_exp(result):
    ans = []
    str_exp = ""
    for x in result:
        if x=='number': pass
        ans.append(x)
        if x.isdigit()==True:
            str_exp += str(x)
        else: str_exp += x
