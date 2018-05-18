from app import db


class Ente(db.Model):
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


class Prueba(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))


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