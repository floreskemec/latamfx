from typing import List
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from currencies import get_best_investment, get_currencies

app = FastAPI()

# Allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request and response models
class InvestmentRequest(BaseModel):
    date: str
    budget: float

class InvestmentResponse(BaseModel):
    currencies: List[str]
    amount_invested: float
    profit: float
    percentage_profit: float

# Route for the root path
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    with open("index.html") as f:
        html = f.read()
    return html

@app.get("/currencies")
def read_currencies():
    return get_currencies()


@app.get("/best-investment", response_model=InvestmentResponse)
def read_best_investment(amount: float, date: str):
    result = get_best_investment(amount=amount, date=date)
    return InvestmentResponse(
        currencies=result["currencies"],
        amount_invested=result["amount_invested"],
        profit=result["profit"],
        percentage_profit=result["percentage_profit"],
    )
