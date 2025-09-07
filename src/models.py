from typing import Literal

from pydantic import BaseModel


class Code(BaseModel):
    code: str | None
    server: str | None
    rewards: str | None
    validity: Literal['Valid', 'Expired']

