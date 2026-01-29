FastAPI Social App

This is a simple social app built with FastAPI where users can sign up, log in, upload images/videos, and view a shared feed.
Media files are stored on ImageKit, and the app uses JWT authentication.

There’s also a small Streamlit frontend to interact with the backend.

What this app does

User registration & login (JWT based)

Secure password handling (hashed, never stored in plain text)

Upload images or videos

View a feed of posts

Delete your own posts

Basic frontend using Streamlit

Tech used

FastAPI

FastAPI Users

SQLAlchemy (async)

SQLite

ImageKit

Streamlit

Uvicorn

Project structure
fastapi_project/
│
├── app/
│   ├── app.py        # API routes
│   ├── db.py         # Database models & setup
│   ├── images.py     # ImageKit config
│   ├── users.py      # Auth & user logic
│   ├── schemas.py    # Pydantic schemas
│
├── frontend.py       # Streamlit UI
├── main.py           # Server entry point
├── test.db           # SQLite database (auto-created)
├── .env              # Environment variables

Environment variables

Create a .env file in the project root:

IMAGEKIT_PRIVATE_KEY=your_private_key
IMAGEKIT_PUBLIC_KEY=your_public_key
IMAGEKIT_URL_ENDPOINT=https://ik.imagekit.io/your_id

Run the backend

From the project root:

uv run uvicorn app.app:app --reload


Or:

python main.py


API docs will be available at:

http://127.0.0.1:8000/docs

Run the frontend

In another terminal:

streamlit run frontend.py

Notes

test.db is the actual database file
Deleting it resets all data (users, posts, everything).

Passwords are not readable by design. Only hashed values are stored.

This project is meant for learning and development, not production as-is.