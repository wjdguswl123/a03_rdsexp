
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import os
import uvicorn
import database

# 1. FastAPI 객체 생성
app = FastAPI()

# 2. HTML 템플릿 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "../a01_front")
)


# 3. 메인 페이지
@app.get("/")
async def heroList(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="a02_hero.html"
    )


# 4. 영웅 검색 API
@app.get("/api/heros")
def get_emps(nickname: str = "", job_class: str = ""):

    return database.select_heros(nickname, job_class)


# 5. 서버 실행
if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
