import database.base.baseCRUD as crud


db = crud.createCollection("customers")
print(db)