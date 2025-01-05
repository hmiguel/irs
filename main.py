from fastapi import FastAPI, HTTPException
from irs import IRS
from models import IRSRequest
from datetime import datetime
import json
import logging

logging.basicConfig(level=logging.DEBUG)

app = FastAPI(title = "IRS API")
metadata = json.load(open("metadata.json"))

@app.get("/")
def read_root():
    return {"status": "Running!"}

@app.post("/irs", description="Calculate IRS for a given year.")
def post_calculate_irs(request: IRSRequest = None):

    year = str(request.year or datetime.now().year-1)

    if year not in metadata.keys():
        raise HTTPException(status_code=404, detail=f"Year {year} not found.")
    
    irs = IRS(metadata.get(year), request.global_income, request.withhold, request.deductions, request.county)
    
    return {
        "year": int(year),
        "global_income": irs.gross_income,
        "colectable_income": irs.colectable_income,
        "total_income_for_tax_purposes": irs.total_income_for_tax_purposes,
        "amount_calculated": irs.amount_calculated,
        "tax_parcel": irs.tax_parcel,
        "total_collected": irs.total_collected,
        "deductions": irs.deductions,
        "county_tax": irs.county_tax,
        "county_benefit": irs.county_benefit,
        "net_amount": irs.net_amount,
        "withhold": irs.withhold,
        "assessed_tax": irs.assessed_tax,
        "total_value": irs.total_value,
        "effective_tax_rate": irs.effective_tax_rate
    }

@app.get("/counties", description="Get the counties tax info for a given year.")
def get_counties_taxes(year: int = None):
    year = str(year or datetime.now().year-1)
    return metadata.get(year, {}).get("county_tax", {})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)