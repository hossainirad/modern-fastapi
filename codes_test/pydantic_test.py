from typing import Optional
from pydantic import BaseModel

class Smart(BaseModel):
    id1: int
    id2: int
    id3: Optional[int] = None

    def __init__(self, id1, id2, id3) -> None:
        print(id1 + id2)




s = Smart(id1='3', id2='4')

