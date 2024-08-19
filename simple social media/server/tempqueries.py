from models import Post
from database import SessionLocal
from datetime import datetime

db = SessionLocal()



# for i in range(300):
#     p = Post(subject="Test " + str(i), content="This is test number " + str(i) + " on this app", created_at=datetime.now())
#     db.add(p)

# db.commit()

# db.close()

# import secrets

# print(secrets.token_hex(32))