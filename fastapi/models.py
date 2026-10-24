from pydantic import BaseModel


class product(BaseModel):
    id: int
    name: str
    discription: str
    price: int
    quantity: int
