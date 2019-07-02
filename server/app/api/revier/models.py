from app.database import db, BaseMixin
from app.serializer import ma
from marshmallow.fields import Nested

class Revier(db.Model, BaseMixin):
    __tablename__ = "reviere"

    reviername = db.Column(db.String)
    ort = db.Column(db.String)
    grenzen = db.relationship('GrenzPunkt', backref="Revier", lazy=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    #tagebucheintraege = db.relationship("TagebuchEintrag", backref="Revier", lazy=False)
    #revier_gäste
    #einrichtungen

    def __init__(self, reviername, ort, user_id):
        self.user_id = user_id
        self.reviername = reviername
        self.ort = ort


class GrenzPunkt(db.Model, BaseMixin):
    __tablename__ = "grenzPunkte"

    revier_id = db.Column(db.Integer, db.ForeignKey("reviere.id"))
    long = db.Column(db.Float)
    lat = db.Column(db.Float)

    def __init__(self, revier_id, long, lat):
        self.revier_id = revier_id
        self.long = long
        self.lat = lat

class Einrichtung(db.Model, BaseMixin):
    __tablename__ = "einrichtungen"

    einrichtungsTyp = db.Column(db.Integer)
    bezeichnung = db.Column(db.String)
    pos_long = db.Column(db.Float)
    pos_lat = db.Column(db.Float)

    def __init__(self, )

class GrenzPunktSchema(ma.ModelSchema):
    class Meta:
        model = GrenzPunkt
        fields = (
            "id",
            "long",
            "lat"
        )

class RevierSchema(ma.ModelSchema):
    grenzen = Nested(GrenzPunktSchema, many=True)
    
    class Meta:
        model = Revier
        fields = (
            "id",
            "grenzen",
            "reviername",
            "ort"
        )