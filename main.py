from fastapi import FastAPI;
from utils import get_data, gen_respone;

app = FastAPI();

@app.get("/")
async def root():
    return {"message": "Hello World"};


@app.get('/product/{category}/')
async def read_item(page: int = 0, category: str = ''):
    
    data = get_data('Elektronik', page);
    respone = gen_respone(data);
    
    return respone;