from quart_db import Connection

#does the actual migratual
async def migrate(connection: Connection) -> None:
    await connection.execute(
        """CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
            )""",
    )

async def valid_migration(connection: Connection) -> bool:
    return True
#will check that migration is valid