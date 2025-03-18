from pydantic import BaseModel
from typing import Any
from fastapi import Body, FastAPI

class User(BaseModel):
    user_id: int
    reservation_id: int

app = FastAPI()

@app.post("/authentication/")
def read_root(user_data: User):
    # Logica di autenticazione qui
    return {"status": "loading", "user_id": user_data.user_id}

@app.get("/test")  # Endpoint per testare l'app
def test():
    return {"ok"}  # Restituisce un messaggio di conferma

@app.post('/test2')
async def update_item(
        payload: Any = Body(None)
):
    return payload