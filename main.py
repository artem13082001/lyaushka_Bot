from fastapi import FastAPI
import uvicorn
from api.routers.user import router_user
from api.routers.case import router_case
from api.routers.inventory import router_inventory
from api.routers.trade import router_trade

app = FastAPI()
app.include_router(router_case)
app.include_router(router_inventory)
app.include_router(router_user)

if __name__ ==  '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)