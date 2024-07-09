from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
# import random
# import string
import numpy as np
import cv2
import easyocr
import paddleocr
import io
import json

# EasyOCR 모델 초기화
reader = easyocr.Reader(['en', 'ko'])  # 지원할 언어 설정

# PaddleOCR 리더 초기화
ocr = paddleocr.PaddleOCR(
    use_angle_cls=True, 
    lang='korean', 
    det_model_dir='/root/.paddleocr/whl/det/ml/Multilingual_PP-OCRv3_det_infer',
    rec_model_dir='/root/.paddleocr/whl/rec/korean/korean_PP-OCRv4_rec_infer'
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/easyocr")
async def easyocr_upload_image(file: UploadFile):
    # 이미지 파일 읽기
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # EasyOCR로 텍스트 추출
    result = reader.readtext(image)

    # OCR 결과를 JSON 형태로 가공
    easy_ocr_results = []
    for (bbox, text, prob) in result:
        ocr_result = {
            "text": text,
            "probability": prob,
            "bounding_box": {
                "bottom_left": [float(coord) for coord in bbox[0]], # 좌표를 float로 변환
                "bottom_right": [float(coord) for coord in bbox[1]],
                "top_right": [float(coord) for coord in bbox[2]],
                "top_left": [float(coord) for coord in bbox[3]],  
            }
        }
        easy_ocr_results.append(ocr_result)

    # # JSON 형식으로 변환
    # easy_ocr_results_json = json.dumps(easy_ocr_results, ensure_ascii=False)

    # 추출된 텍스트를 JSON 형태로 반환
    text_results = [{"text": res[1], "confidence": res[2]} for res in result]
    return {"filename": file.filename, "results": easy_ocr_results}


@app.post("/padlocr")
async def padlocr_upload_image(file: UploadFile):
    # 이미지 파일 읽기
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # 이미지 읽기 및 OCR 수행
    result = ocr.ocr(image, cls=True)

    paddle_ocr_results = []
    for bounding_box, ocr_result in result[0]:

        text = ocr_result[0]
        probability = float(ocr_result[1])  # 확률을 float로 변환
        bottom_left = [float(coord) for coord in bounding_box[0]]  # 좌표를 float로 변환
        bottom_right = [float(coord) for coord in bounding_box[1]]
        top_right = [float(coord) for coord in bounding_box[2]]
        top_left = [float(coord) for coord in bounding_box[3]]
        
        paddle_ocr_result = {
            "text": text,
            "probability": probability,
            "bounding_box": {
                "bottom_left": bottom_left,
                "bottom_right": bottom_right,
                "top_right": top_right,
                "top_left": top_left
            }
        }
        paddle_ocr_results.append(paddle_ocr_result)

    # # JSON convert
    # paddle_ocr_results_json = json.dumps(paddle_ocr_results, ensure_ascii=False, indent=4)

    # # JSON 출력
    # print(paddle_ocr_results_json)

    # 추출된 텍스트를 JSON 형태로 반환
    # text_results = [{"text": res[1], "confidence": res[2]} for res in result]
    return {"filename": file.filename, "results": paddle_ocr_results}