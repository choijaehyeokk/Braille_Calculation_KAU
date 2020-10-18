from django.shortcuts import render
from .models import Braille

from .modules.model import *
from .modules.ImageProc import *
from .modules.calculation import *

import os

# Create your views here.
def home(request):
    return render(request,'home.html')


def braille_image_upload(request):
    braille_image = Braille()
    braille_image.images = request.FILES['images']
    braille_image.save()

    return render(request,'home.html')

def calculation(request):
    b_image = Braille.objects.last()

    return render(request,'calculation.html',{'b_image':b_image})

def calculation(request):
    b_image = Braille.objects.last()
    #여기서 이제 b_image를 가지고 계산

    final_str = ""
    result = None
    #_load_model_from_path('./BrailleRecogModel.h5')
    #print(gModel)

    if request.method == 'POST':
        # 원본 이미지의 경로를 받아옴
        imgProc = ImgProc(b_image.images.path)
        
        imgProc.setImg()  # 경로에서 이미지를 세팅
        predictPath = "./media/predict"
        imgProc.createPredictDir(predictPath)  # 예측 가능한 이미지를 위한 디렉토리 생성

        imgProc.cutting()  # 원본 이미지를 예측 가능한 이미지로 분할

        pred = action(predictPath)
        print(pred)
        
        final = []
        for i in range(len(pred)):
            if pred[i] == 'number' or pred[i]=='=':
                continue
            elif pred[i - 1] == '/' and pred[i]=='/':
                continue
            else:
                final.append(pred[i])
        final_str = ""
        for i in final:
            final_str += i

        result = postfix(pre_to_postfix(final_str))

        print(f'식 : {final_str}')
        print(f'정답 : {result}')

        # imgProc.checkOrigin()   # 원본 이미지 확인
        # imgProc.checkPredict(0) # 예측 가능한 이미지들 확인, index번째 이미지 확인, index가 -1이면 모두 확인
        # print(imgProc)          # 객체 정보 표시
        
        imgProc.removePredictDir()  # 예측 가능한 이미지를 위한 디렉토리 삭제
    
    return render(request,'calculation.html',{'b_image':b_image,'final_str':final_str, 'result':result})
    