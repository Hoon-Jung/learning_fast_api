from models import Post
from database import SessionLocal
from datetime import datetime

db = SessionLocal()

p = Post(subject="Welcome", content="This is the first of many posts for this app", created_at=datetime.now())
db.add(p)
db.commit()

db.close()