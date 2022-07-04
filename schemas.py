from marshmallow import Schema, fields

class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre = fields.Str()
    director = fields.Str()

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()

director_schema = DirectorSchema()
director_schema = DirectorSchema(many=True)

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()

genre_schema = GenreSchema()
genre_schema = GenreSchema(many=True)

   
