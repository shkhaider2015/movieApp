from movieApp import db


actors = db.Table('actors',
                  db.Column('movie_id', db.Integer, db.ForeignKey('movie.movie_id'), primary_key=True),
                  db.Column('actor_id', db.Ineteger, db.ForeignKey('actor.actor_id'), primary_key=True)
                  )


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(30), unique=False, nullable=False)
    movie_industry = db.Column(db.String(30), unique=False, nullable=False)
    movie_genr = db.Column(db.String(30), unique=False,
                           nullable=True, default="movies")
    movie_image = db.Column(db.String(50), nullable=False,
                            default="movie_image.jpg")
    release_date = db.Column(db.String(12))
    cast = db.relationship('Actor', secondary=actors, lazy='subquery',
                           backref=db.backref('movies', lazy=True)
                           )


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    actor_name = db.Column(db.String(30), unique=False, nullable=False)
    actor_gender = db.Column(db.String(10), nullable=False,
                             default="Not specify")
    actor_image = db.Column(db.String(50), nullable=False,
                            default="actor_image.jpg")
    actor_age = db.Column(db.Integer)
