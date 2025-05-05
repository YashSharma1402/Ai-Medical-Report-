from fastapi import FastAPI
from pydantic import BaseModel
from app.utils import analyze_report

app = FastAPI()

class ReportRequest(BaseModel):
    content: str

@app.post("/analyze")
def analyze(report: ReportRequest):
    result = analyze_report(report.content)
    return {"summary": result}
