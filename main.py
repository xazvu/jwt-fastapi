import uvicorn
from sqlalchemy.testing.pickleable import User

import models
from fastapi import FastAPI, status, Depends, HTTPException
from database import init_db, delete_db
from typing import Annotated
from sqlalchemy.orm import Session
from auth import get_db, router, get_current_user

init_db()

# delete_db()

app = FastAPI()
app.include_router(router)

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return {'User': user}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)