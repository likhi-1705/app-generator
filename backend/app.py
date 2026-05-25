from fastapi import FastAPI

from pipeline.intent_parser import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schemas
from pipeline.validator import validate_output
from pipeline.repair_engine import repair
from pipeline.executor import execution_test

app = FastAPI()

@app.get("/")
def home():
    return {"message": "App Generator Running"}

@app.post("/generate")
def generate(prompt: str):

    intent = extract_intent(prompt)

    blueprint = design_system(intent)

    result = generate_schemas(blueprint)

    if not validate_output(result):
        result = repair(result)

    result["execution_status"] = execution_test(result)

    return result