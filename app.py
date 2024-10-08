from quart import g, Quart
from quart_db import QuartDB
from quart_schema import QuartSchema, validate_request, validate_response
from dataclasses import dataclass
from migrations import migrate
#app is the variable that holds the quart application object
app=Quart(__name__)
##name tells quart the module name(the file that contains the code)
QuartDB(app, url="sqlite:///database.db")#connects to db
QuartSchema(app)

async def startup():
    async with app.db.connection() as connection:
        await migrate(connection)
        
async def before_request():
    g.connection = await app.db.connection()
#a dataclass holds data and @dataclass is the decorator, which generates special methods for that class
@dataclass
class CardInput:
    question: str
    answer: str

@dataclass
class Card(CardInput):
    id: int

#route decorator (@) defiend a route that responds to get requests
@app.post("/cards/")
@validate_request(CardInput)
@validate_response(Card)
#function is called whenever a get request is made to route "/"
async def create_card(data: CardInput) -> Card:
    """Create a new Anki Card"""
    result = await g.connection.fetch_one(
        """INSERT INTO cards (question, answer)
                VALUES (:question, :answer)
                RETURNING id, question, answer""",
                {"question": data.question, "answer": data.answer},
    )
    return Card(**result)

