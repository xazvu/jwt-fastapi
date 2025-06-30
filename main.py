import uvicorn
import models
from fastapi import FastAPI, status, Depends, HTTPException
from database import init_db, delete_db
from typing import Annotated
from sqlalchemy.orm import Session
from auth import get_db, router

init_db()

# delete_db()

app = FastAPI()
app.include_router(router)

db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: None, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return {'User': user}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)