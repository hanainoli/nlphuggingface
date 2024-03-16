from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Specify the model by its name
classifier = pipeline("sentiment-analysis")
app = FastAPI()

data = ["I love u", "I hate you"]

classifier(data)

class RequestModel(BaseModel):
    input_string: str
@app.post("/analyse")
def your_function(request: RequestModel):
        input_string = request.input_string
        sentiment = classifier(input_string)
        return {"result":
            { "sentiment" : sentiment[0]["label"],
            "score" : sentiment[0]["score"]
            }
        }