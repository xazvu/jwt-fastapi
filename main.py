import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "fast api jwt"}

if __name__ == "__main__":
    # models.Base.metadata.drop_all(bind=engine)
    uvicorn.run(app, host="127.0.0.1", port=8000)