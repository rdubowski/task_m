from fastapi import FastAPI

app = FastAPI()


# @app.post("/encode")
# def encode():
#     return {"shortened_url": ""}

@app.get("/decode")
async def decode():
    return {"original_url": ""}