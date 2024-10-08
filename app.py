from quart import Quart
from quart_db import QuartDB

#app is the variable that holds the quart application object
app=Quart(__name__)
##name tells quart the module name(the file that contains the code)
QuartDB(app, url="sqlite:///database.db")#connects to db

#route decorator (@) defiend a route that responds to get requests
@app.get("/")
#index function is called whenever a get request is made to route "/"
async def index():
    return {"Hello": "world"}