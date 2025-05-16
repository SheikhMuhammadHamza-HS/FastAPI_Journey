from fastapi import FastAPI
from pydantic import BaseModel

class ChatMessage(BaseModel): 
    role: str
    content: str

class ChatInput(BaseModel): #nesting pydantic models
    # message: list[dict]  # [{"role": "user", "content": "Hello"}]
    # [{"role": "user", "content": "Hello"}]
    messages: list[ChatMessage]

app = FastAPI()


@app.get("/health")  # err page not found
def health_check():
    return {"message": "Hello, Agentic AI online class"}


@app.post("/chat")
def chat(data_received: ChatInput):
    print("Chat Input:", data_received)
    print("Chat Input Type", type(data_received.messages))
    print("Chat Message:", data_received.messages)
    print("Chat Message Type", type(data_received.messages))
    
    return {"message": "Hello, Agentic AI online class"}





# @app.get("/health")  # err page not found
@app.get("/")  # get API endpoint
def hello_message():
    return {"Hello": "Agentic AI online class"}
   

@app.post("/chat/start") # post API endpoint
def status(messages:dict):
    print("Data received:", messages)
    # Business logic
    return messages

def test_hello_message():
    assert hello_message() ==  {"Hello": "Agentic"}
    
    
if __name__ == "__main__":
    print("calling hello_message()")    
    test_hello_message()
    