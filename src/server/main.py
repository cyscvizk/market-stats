import uvicorn
from fastapi import FastAPI
from server.api.routes import router
from server.core.config import config


app = FastAPI(title="Simple FastAPI Server")

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        "server.main:app",
        host=config.host,
        port=config.port,
        log_level=config.log_level.lower(),
        reload=True
    )
