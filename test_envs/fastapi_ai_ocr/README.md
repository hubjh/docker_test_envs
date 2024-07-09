# fastapi 실습환경 base python 3.10 버전

requirements.txt에 원하는 python 모듈 추가

# 접근 방법
vscode에서 wsl_connect 접근하여 사용 가능

local(windows10) -> wsl2(Ubuntu 22.04)

컨테이너를 띄워놓고 wsl2에서 vscode로 main.py 수정하면 fastapi server가 reload 되면서 api 기능 추가

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def read_test():
    return {"Reload": "test"}
```



다른 컨테이너 docker-compose.yml에  
```
    extra_hosts:
      - 'host.docker.internal:172.17.0.1'
```

를 추가하면 컨테이너 내부에서 로컬 포트에 접근 가능


컨테이너 내부에서 python & jupyter 로 사용
```
import requests

response = requests.get('http://host.docker.internal:8000/test')
print(response.content)
```