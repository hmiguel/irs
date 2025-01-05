from pydantic import BaseModel
from datetime import date

class IRSRequest(BaseModel):
    year : int = date.today().year - 1
    global_income: float = 0
    county: str = None
    withhold: float = 0
    deductions: float = 0