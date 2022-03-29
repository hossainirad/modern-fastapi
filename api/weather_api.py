import fastapi
from starlette.requests import Request

router = fastapi.APIRouter()

@router.get('/api')
def weather(request: Request):
    return 'yes'
