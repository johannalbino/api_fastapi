import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from mangum import Mangum
from src.routers import consult_api_spacex_router


app = FastAPI(
    title="API FastAPI",
    docs_url="/docs",
    redoc_url="/redocs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"]
)

app.include_router(consult_api_spacex_router)


handler = Mangum(app)


if __name__ == "__main__":
    uvicorn.run(
        app if os.getenv("ENVIRONMENT") == "prod" else "app:app",
        workers=2,
        reload=True
    )
