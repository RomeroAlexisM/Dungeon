from flask_user import UserMixin, SQLAlchemyAdapter, UserManager
from api.app import db, app


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.url,
            'active': self.active
        }


db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)


class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    level = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    mana = db.Column(db.Integer)
    strength = db.Column(db.Integer)
    agility = db.Column(db.Integer)
    vitality = db.Column(db.Integer)
    energy = db.Column(db.Integer)
    physical_def = db.Column(db.Integer)
    magical_def = db.Column(db.Integer)
    status = db.Column(db.String(50))
    attacks_id = db.Column(db.Integer)
    exp = db.Column(db.Integer)
    covenant = db.Column(db.String(60))
    type = db.Column(db.String(60))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'level': self.level,
            'hp': self.hp,
            'mana': self.mana,
            'strength': self.strength,
            'agility': self.agility,
            'vitality': self.vitality,
            'energy': self.energy,
            'physical_def': self.physical_def,
            'magical_def': self.magic_def,
            'status': self.status,          #ENVENENADO, INCENDIADO, SANO, etc
            'attacks_id': self.attacks_id,
            'exp': self.exp,
            'race': self.race,              #  HUMANO, BESTIA, ETÉREO (en inglés)
            'covenant': self.covenant,      #PACTOS PARA QUEST (FUTURO)
            'type': self.type               #  Acá va a ser si es PLAYABLE, ENEMY o NPC
        }


class Attribute(object):
    def __init__(self, hp, mana, strength, agility, vitality, energy):
        self.hp = hp
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.vitality = vitality
        self.energy = energy


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(50))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url
        }