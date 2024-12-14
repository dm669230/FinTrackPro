from pydantic import BaseModel
from typing import Optional, List, Dict, Union

class NewLoanRegisterSchema(BaseModel):
    user_id: Optional[int] = None
    loan_amount: Optional[float] = None
    loan_status: Optional[str] = None
    interest_rate: Optional[float] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None