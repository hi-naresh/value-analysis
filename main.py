from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.endpoints import router as api_router
from src.core.config import settings
from src.utils.logging import logger


app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
async def startup_event():
    logger.info("Application startup complete.")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown complete.")

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to value analyzer!"}


# if __name__ == "__main__":
#     import uvicorn
#     logger.info("Starting Uvicorn server...")
#     uvicorn.run(app, host="0.0.0.0", port=8001)
