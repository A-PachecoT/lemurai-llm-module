from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from lemur_core import handle_query

app = FastAPI()


class Query(BaseModel):
    text: str


@app.post("/query/")
async def get_response(query: Query):
    try:
        response = handle_query(query.text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
