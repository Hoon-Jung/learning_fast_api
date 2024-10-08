from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from domain.user import user_CRUD, user_schema

from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from domain.user.user_CRUD import pwd_context

router = APIRouter(prefix = "/api/user")

ACCESS_TOKEN_EXPIRE_MINUTES = 60*24
SECRET_KEY = "cb38f98155bfd63b298208749d490d365388f50b6f1e7459b57667a2c26d1fe2"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(
    _user_create: user_schema.UserCreate,
    db: Session = Depends(get_db)):

    #check for a duplicate email or username
    same_user = user_CRUD.get_existing_user(db, user_create=_user_create)
    if same_user:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Username or email already exists")

    user_CRUD.create_user(db, user_create=_user_create)


@router.post("/login")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)):
    user = user_CRUD.get_curr_user(db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    data = {
        "sub": user.username,
        "exp": datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token=jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username,
    }

def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    else:
        user = user_CRUD.get_curr_user(db, username=username)
        if user is None:
            raise credentials_exception
        return user