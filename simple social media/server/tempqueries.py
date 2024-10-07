from models import Post, Replies, Category
from database import SessionLocal
from datetime import datetime

db = SessionLocal()

# c1 = Category(subject = "Humor")
# c2 = Category(subject = "Technology")
# c3 = Category(subject = "Movies & TV")
# c4 = Category(subject = "Video Games")
# c5 = Category(subject = "Fashion")

# db.add(c1)
# db.add(c2)
# db.add(c3)
# db.add(c4)
# db.add(c5)
# db.commit()

import random

posts = db.query(Post).all()
for p in posts:
    p.category_id = random.choice([1, 2, 3, 4, 5])
db.commit()
