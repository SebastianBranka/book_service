from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def test_endpoint():
    return {"message": "This is a test endpoint!"}
