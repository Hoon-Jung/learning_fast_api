from models import Post
from sqlalchemy.orm import Session


def get_all_posts(db: Session):
    return db.query(Post).order_by(Post.created_at.desc()).all()

def get_specific_post(db: Session, id):
    return db.query(Post).get(id)