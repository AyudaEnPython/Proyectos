"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, asdict
# pip install prototools
from prototools import ProtoSqlite, tabulate, Menu

HEADERS = "Id", "Descripcion", "Autor", "Editorial"


@dataclass
class Comic:
    comic_id: int
    descripcion: str
    autor_id: int
    editorial_id: int

    def get_data(self):
        return asdict(self)


class Database(Menu):

    def __init__(self):
        super().__init__()
        self._table = "comics"
        self._db = ProtoSqlite("data.db", lang="es")
        self._pk = "comic_id"
        self.add_options(
            ("Ver comics", self.ver),
        )

    def insertar(self, obj: object) -> None:
        self._db.add(self._table, obj.get_data())

    def actualizar(self, query: str, id_: int) -> None:
        _s = f"{self._pk} = {id_}"
        self._db.update(self._table, query, _s)

    def eliminar(self, obj: object) -> None:
        pk = str(obj.get_data()[self._pk])
        self._db.delete(self._table, self._pk, pk)

    def seleccionar(self) -> None:
        data = self._db.get_all(self._table)
        return data

    def ver(self):
        data = self.seleccionar()
        print(tabulate(data, headers=HEADERS))


if __name__ == "__main__":
    db = Database()
    db.insertar(Comic(1, "X-Men #1", 1, 1))
    db.insertar(Comic(2, "X-Men #2", 1, 1))
    print(tabulate(db.seleccionar(), headers=HEADERS))
    db.insertar(Comic(3, "X-Men #31", 1, 2))
    print(tabulate(db.seleccionar(), headers=HEADERS))
    db.actualizar("editorial_id=1", 3)
    db.actualizar("descripcion='X-Men #3'", 3)
    print(db.seleccionar())
    print(tabulate(db.seleccionar(), headers=HEADERS))
    # app = Database()
    # app.run()
