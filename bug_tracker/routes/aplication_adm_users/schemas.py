from pydantic import BaseModel


class AplicationUserAdmSchema(BaseModel):
    name: str
    email: str
    password : str
    


class PublicAplicationUserAdmSchema(BaseModel):
    id: int
    name: str
    email: str