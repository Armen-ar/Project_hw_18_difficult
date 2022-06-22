from app.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, aid):
        return self.session.query(Genre).get(aid)

    def get_all(self):
        return self.session.query(Genre).all()
