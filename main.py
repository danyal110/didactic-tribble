from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello Duke"}


@app.get("/add/{num1}/{num2}")
async def add_numbers(num1: int, num2: int):
    return {"result": num1 + num2}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
