from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter

from api.app import db, app


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())


db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)

class Playable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    nivel = db.Column(db.Integer)
    ps = db.Column(db.Integer)
    mana = db.Column(db.Integer)
    fuerza = db.Column(db.Integer)
    agilidad = db.Column(db.Integer)
    vitalidad = db.Column(db.Integer)
    energia = db.Column(db.Integer)
    defensafisica = db.Column(db.Integer)
    defensamagica = db.Column(db.Integer)
    estado = db.Column(db.String(50))
    ataque_id = db.Column(db.Integer)
    experiencia = db.Column(db.Integer)
    pacto = db.Column(db.String(60))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'nivel': self.nivel,
            'ps': self.ps,
            'mana': self.mana,
            'fuerza': self.fuerza,
            'agilidad': self.agilidad,
            'vialidad': self.vitalidad,
            'energia': self.energia,
            'defensafisica': self.defensafisica,
            'defensamagica': self.defensamagica,
            'estado': self.estado,
            'ataque_id': self.ataque_id,
            'experiencia': self.experiencia,
            'pacto': self.pacto
        }


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    url = db.Column(db.String(50))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'url': self.url
        }


class Enemy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    nivel = db.Column(db.Integer)
    ps = db.Column(db.Integer)
    mana = db.Column(db.Integer)
    fuerza = db.Column(db.Integer)
    agilidad = db.Column(db.Integer)
    vitalidad = db.Column(db.Integer)
    energia = db.Column(db.Integer)
    defensafisica = db.Column(db.Integer)
    defensamagica = db.Column(db.Integer)
    estado = db.Column(db.String(50))
    ataque_id = db.Column(db.Integer)
    experiencia = db.Column(db.Integer)
    raza = db.Column(db.String(60))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'nivel': self.nivel,
            'ps': self.ps,
            'mana': self.mana,
            'fuerza': self.fuerza,
            'agilidad': self.agilidad,
            'vialidad': self.vitalidad,
            'energia': self.energia,
            'defensafisica': self.defensafisica,
            'defensamagica': self.defensamagica,
            'estado': self.estado,
            'ataque_id': self.ataque_id,
            'experiencia': self.experiencia,
            'raza': self.raza
        }


"""
CREATE TABLE entidades (
    entidad_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    nivel INTEGER NOT NULL,
    ps INTEGER NOT NULL,
    mana INTEGER NOT NULL,
    fuerza INTEGER NOT NULL,
    agilidad INTEGER NOT NULL,
    vitalidad INTEGER NOT NULL,
    energia INTEGER NOT NULL,
    defensafisica INTEGER NOT NULL,
    defensamagica INTEGER NOT NULL,
    ataque INTEGER NOTE NULL,
    estado TEXT NOT NULL,
    exp INTEGER NOT NULL,
    pacto TEXT NOT NULL);
"""

"""
CREATE TABLE ataques (
    ataque_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY(entidad) REFERENCES entidad(entidad_id)
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    costomana INTEGER NOT NULL,
    multiplicador REAL NOT NULL,
    especial NUMERIC NOT NULL,
    
"""

"""
    nombre = db.Column(db.String(50))
    self.nombre = str(nombre)
    self.nivel = int(nivel)
    self.ps = int(ps)
    self.mana = int(mana)
    self.fuerza = int(fuerza)
    self.agilidad = int(agilidad)
    self.vitalidad = int(vitalidad)
    self.energia = int(energia)
    self.defensafisica = int(defensafisica)
    self.defensamagica = int(defensamagica)
    self.estado = str(estado)
    self.exp = int(exp)
    self.items = items
    self.ataques = ataques
    self.ataca = False
"""