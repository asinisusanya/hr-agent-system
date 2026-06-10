from pydantic import BaseModel


class RequestModel(BaseModel):
    user_id: str
    message: str