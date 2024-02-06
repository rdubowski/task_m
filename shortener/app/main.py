from fastapi import FastAPI

app = FastAPI()


# @app.post("/encode")
# def encode():
#     return {"shortened_url": ""}

@app.get("/decode")
async def decode() -> dict[str, str]:
    return {"original_url": ""}