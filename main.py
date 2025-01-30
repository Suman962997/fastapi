from fastapi import FastAPI 
from crud import router as user_router


app=FastAPI()
app.include_router(user_router)

@app.get("/")
def main():
    return {"HOME"}