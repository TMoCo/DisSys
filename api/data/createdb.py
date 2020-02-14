from api import db
from api.data.countries import locations
from api.data.models import Location


def populate():
    db.create_all()

    count = 1
    for l in locations:
        new_location = Location(id=count, country=locations[l][0], \
                            capital=locations[l][1], langCode=locations[l][2], \
                            latitude=locations[l][3], longitude=locations[l][4])
        db.session.add(new_location)
        count += 1
    db.session.commit()
