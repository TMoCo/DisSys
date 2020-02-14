from api import db

class Location(db.Model):
    __tablename__ = 'Locations'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(64))
    capital = db.Column(db.String(64))
    langCode = db.Column(db.String(10))
    latitude = db.Column(db.String(7))
    longitude = db.Column(db.String(7))

    def __repr__(self):
        return "<Location(country='%s', capital='%s', code='%s', lat='%s',lon='%s')>\n"\
         % (self.country,self.capital,self.langCode, self.latitude,self.longitude)
