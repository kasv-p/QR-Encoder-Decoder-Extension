from fastapi import FastAPI
from endpoints import qr_encoder, qr_decoder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(qr_encoder.router)
app.include_router(qr_decoder.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"], 
    allow_headers=["*"],  
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload="True")
