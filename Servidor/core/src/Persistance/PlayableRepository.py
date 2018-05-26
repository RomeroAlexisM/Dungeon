from flask import session
from sqlalchemy import Integer
from sqlalchemy.dialects.mysql import json
import json
import api

from api.app import Session, db
from api.models import Playable
from sqlalchemy.sql import column, text


class PlayableRepository():
    def getFirst(self):
        session = Session()
        session.query(Playable).first()

    def getAll(self):
        session = Session()
        return session.query(Playable).all()

    def get_attributes(self, playable_id):
        print(playable_id)
        session = Session()

        for ps, mana, fuerza, agilidad, vitalidad, energia in session.query(Playable.ps, Playable.mana, Playable.fuerza,
                                                                            Playable.agilidad, Playable.vitalidad,
                                                                            Playable.energia).filter_by(id=playable_id):
            atributo = api.models.Attribute(ps, mana, fuerza, agilidad, vitalidad, energia)
            print(ps, mana, fuerza, agilidad, vitalidad, energia)

        return atributo
