import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from loguru import logger

from .v1 import router as router_v1
from api.utils import check_openai_api

logger.debug('Checking OpenAI API ...')
if not check_openai_api():
    exit(-1)

app = FastAPI(
    title='MobileGPT',
    redoc_url=None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/files", StaticFiles(directory="static", html=True), name="static")


routers = [router_v1]
[app.include_router(_router) for _router in routers]

def create_app():
    logger.debug('Starting API ...')
    return app
