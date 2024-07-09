from fastapi import FastAPI
from pydantic import BaseModel
import random
import string

def generate_random_string(length: int) -> str:
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_int(max_value: int) -> int:
    return random.randint(1, max_value)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def read_test():
    return {"Reload": "test"}

@app.get("/random")
def get_random_data():
    random_string = generate_random_string(10)  # 길이 10의 랜덤 문자열 생성
    random_int = generate_random_int(100)  # 1부터 100 사이의 랜덤 정수 생성
    return {"one": random_string, "two": random_int}