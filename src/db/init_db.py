import os
from objectbox import Store, Model
from src.db.schema.document import Document


class Database:
    def __init__(self, db_dir="../data/rag2-db"):
        self.db_dir = db_dir
        self.store = None
        self.document_box = None

    def initialize(self):
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir)

        model = Model()
        model.entity(Document)
        self.store = Store(model=model, directory=self.db_dir)
        self.document_box = self.store.box(Document)
        print("Database initialized")

    def get_document_box(self):
        if self.document_box is None:
            raise Exception("Database is not initialized")
        return self.document_box

    def close(self):
        if self.store:
            self.store.close()
            self.store = None
            self.document_box = None
            print("Database closed")
