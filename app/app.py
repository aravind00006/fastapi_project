from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
    
app = FastAPI(lifespan=lifespan)

text_posts = {
    1: {"title": "midnight_thoughts", "content": "Why does everything feel heavier at night?"},
    2: {"title": "small_wins", "content": "Progress is quiet, but it still counts."},
    3: {"title": "burnout_mode", "content": "I’m tired, but I’m not done."},
    4: {"title": "overthinking", "content": "My brain won’t stop running marathons."},
    5: {"title": "reset_day", "content": "Starting over is still moving forward."},
    6: {"title": "focus_check", "content": "Discipline beats motivation every time."},
    7: {"title": "self_talk", "content": "I need to be kinder to myself."},
    8: {"title": "future_me", "content": "I hope I’m proud of this version of me."},
    9: {"title": "grind_hours", "content": "No one sees the work behind the scenes."},
    10: {"title": "calm_before", "content": "Peace is learning to pause."}
}

@app.get("/")
def root():
    return {"status": "API is running"}

@app.get("/hello-world")
def hello_world():
    return {"message": "Hello World"}

@app.get('/post')
def get_post(limit:int):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get('/post/{id}')
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code= 404, detail='post not found')
    return text_posts.get(id)

@app.post("/posts")
def create_post(post:PostCreate):
    new_post = {'title':post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
