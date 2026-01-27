from fastapi import FastAPI, HTTPException

app = FastAPI()

test_posts = {1: {"title": "new_post", 'content': 'why am i doing this?'},
        2: {"title": "new_post", 'content': '2why am i doing this?'},
        3: {"title": "new_post", 'content': '3why am i doing this?'},
        4: {"title": "new_post", 'content': '4why am i doing this?'},
        5: {"title": "new_post", 'content': '5why am i doing this?'}}

@app.get("/")
def root():
    return {"status": "API is running"}

@app.get("/hello-world")
def hello_world():
    return {"message": "Hello World"}

@app.get('/post')
def get_post(limit:int):
    if limit:
        return list(test_posts.values())[:limit]
    return test_posts

@app.get('/post/{id}')
def get_post(id:int):
    if id not in test_posts:
        raise HTTPException(status_code= 404, detail='post not found')
    return test_posts.get(id)