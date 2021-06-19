from fastapi import APIRouter
from starlette.responses import JSONResponse
from src.handlers.consult_api_spacex import handler_consult_api_spacex

consult_api_spacex_router = APIRouter()


@consult_api_spacex_router.get("/consult-api-spacex")
async def consult_api_spacex():
    data = await handler_consult_api_spacex()
    if isinstance(data, int):
        return JSONResponse(status_code=data, content={"Detail": "An error occurred while trying to query."})
    else:
        return JSONResponse(status_code=200, content=data)
