#!/usr/bin/env python3

from app import app
from models import db, Plant

with app.app_context():

    Plant.query.delete()

    aloe = Plant(
        id=1,
        name="Aloe",
        image="./images/aloe.jpg",
        price=11.50,
    )

    zz_plant = Plant(
        id=2,
        name="ZZ Plant",
        image="./images/zz-plant.jpg",
        price=25.98,
    )

    db.session.add_all([aloe, zz_plant])
    db.session.commit()


#!/usr/bin/env python3

# from random import choice as rc
# from faker import Faker

# from app import app
# from models import db, Plant

# fake = Faker()

# def make_plants():
#     Plant.query.delete()

#     plants = [
#         Plant(name="Aloe", image="https://example.com/aloe.jpg", price=11.50),
#         Plant(name="ZZ Plant", image="https://example.com/zz-plant.jpg", price=25.98)
#     ]

#     for _ in range(18):
#         plant = Plant(
#             name=fake.word(),
#             image=fake.image_url(),
#             price=round(fake.random_number(digits=2), 2)
#         )
#         plants.append(plant)

#     db.session.add_all(plants)
#     db.session.commit()

# if __name__ == '__main__':
#     with app.app_context():
#         make_plants()
