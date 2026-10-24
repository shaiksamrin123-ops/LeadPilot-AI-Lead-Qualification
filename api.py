from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from lead_logic import qualify_lead_logic

app = FastAPI(
    title="LeadPilot API",
    description="API for lead qualification and prioritization",
    version="1.0.0"
)


class LeadRequest(BaseModel):
    customer_name: str = Field(min_length=1)
    budget: float = Field(ge=0)
    interest_level: str
    urgency: str


@app.post("/qualify-lead")
def qualify_lead_api(lead: LeadRequest):
    try:
        return qualify_lead_logic(**lead.model_dump())
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))
