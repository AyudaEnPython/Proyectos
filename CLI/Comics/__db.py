# pip install prototools
from prototools import ProtoSqlite

db = ProtoSqlite("data.db", lang="es")

if __name__ == "__main__":
    db.create_table(
        "comics",
        "comic_id INTEGER, descripcion TEXT, "
        "autor_id INTEGER, editorial_id INTEGER, "
        "PRIMARY KEY (comic_id)",
    )
