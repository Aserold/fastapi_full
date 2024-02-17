from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

from fastapi import FastAPI

app = FastAPI(
    title='Trading App'
)


fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Jake'},
    {'id': 2, 'role': 'investor', 'name': 'John'},
    {'id': 3, 'role': 'trader', 'name': 'Mary'},
    {'id': 4, 'role': 'investor', 'name': 'Peter', 'degree': [
        {'id': 1, 'created_at': '2020-01-01', 'type_degree': "expert"}
    ]},
]


class DegreeType(Enum):
    novice = 'novice'
    expert = 'expert'


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = None


@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': "BTC", 'side': "buy", 'price': 123, 'amount': 2.12},
    {'id': 2, 'user_id': 1, 'currency': "BTC", 'side': "sell", 'price': 125, 'amount': 2.12},
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}
