from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domain.post import post_router
from domain.replies import replies_router
from domain.user import user_router

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello")
# def read_root():
#     return {"message": "Welcome"}

#api/post/list/...

app.include_router(post_router.router)
app.include_router(replies_router.router)
app.include_router(user_router.router)
app.mount("/assets", StaticFiles(directory="../client/dist/assets"))

@app.get("/")
def index():
    return FileResponse("../client/dist/index.html")