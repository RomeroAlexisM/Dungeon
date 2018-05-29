var Juego = {
  //configuracion de tamaño de mapa

  ancho: 900,
  alto: 500,
  mapaActual: 1,
  pressing: [],
  KEY_LEFT: 37,
  KEY_RIGHT: 39,
  KEY_UP: 38,
  KEY_DOWN: 40,
  entidad: new Entidad(10, ['images/pj/guerreroCaminar1.png'], {width: 32, height: 42}, {stand: [1, 1], run: [9, 16], up: [18, 18], down: [19, 19]}),

  puertas:[
    new Puerta(890,895,360,420),
    new Puerta(110,240,470,490),
    new Puerta(0,-20,10,90),
    new Puerta(885,900,170,480),
    new Puerta(885,900,170,480),
    new Puerta(345,735,0,-20),
    new Puerta(885,900,200,270)
  ],

  paredes:[
    //horizontales
      //mapa1
    new Pared(190,80,680,1,1),
    new Pared(190,490,680,1,1),
    new Pared(0,160,190,1,1),
    new Pared(0,250,190,1,1),
    new Pared(871,360,30,1,1),
    new Pared(871,450,30,1,1),
      //mapa2
    new Pared(0,360,240,1,2),
    new Pared(0,450,100,1,2),
      //mapa3
    new Pared(0,10,100,1,3),
    new Pared(0,100,240,1,3),
    new Pared(110,0,120,1,3),
      //mapa4
    new Pared(191,10,710,1,4),
    new Pared(401,100,499,1,4),
    new Pared(301,120,180,1,4),
    new Pared(401,250,68,1,4),
    new Pared(401,290,130,1,4),
    new Pared(191,370,340,1,4),
    new Pared(531,170,369,1,4),
    new Pared(531,490,369,1,4),
      //mapa5
    new Pared(0,170,900,1,5),
    new Pared(0,490,900,1,5),
      //mapa6
    new Pared(0,170,345,1,6),
    new Pared(0,490,345,1,6),
    new Pared(345,290,130,1,6),
    new Pared(345,370,270,1,6),
    new Pared(615,130,130,1,6),
    new Pared(340,130,145,1,6),
      //mapa7
    new Pared(335,370,140,1,7),
    new Pared(495,190,425,1,7),
    new Pared(605,380,140,1,7),
    new Pared(605,270,295,1,7),
    new Pared(345,500,380,1,7),
      //mapa8
    new Pared(0,190,185,1,8),
    new Pared(0,270,185,1,8),
    new Pared(185,40,700,1,8),
    new Pared(185,430,700,1,8),


    //verticales
      //mapa1
    new Pared(1,170,1,60,1),
    new Pared(199,250,1,240,1),
    new Pared(199,90,1,70,1),
    new Pared(871,450,1,40,1),
    new Pared(871,90,1,280,1),
    new Pared(0,370,1,50,1),
      //mapa2
    new Pared(250,370,1,130,2),
    new Pared(100,450,1,50,2),
      //mapa3
    new Pared(250,0,1,100,3),
      //mapa4
    new Pared(201,0,3,380,4),
    new Pared(301,120,1,140,4),
    new Pared(471,120,1,140,4),
    new Pared(531,170,1,120,4),
    new Pared(531,370,1,120,4),
    new Pared(891,0,1,100,4),
     //mapa5
    new Pared(0,150,1,350,5),
     //mapa6
    new Pared(350,170,1,120,6),
    new Pared(350,370,1,120,6),
    new Pared(615,130,1,240,6),
    new Pared(480,130,1,160,6),
    new Pared(335,0,1,130,6),
    new Pared(750,0,1,130,6),
    new Pared(0,150,1,350,6),
      //mapa7
    new Pared(335,390,1,110,7),
    new Pared(745,380,1,120,7),
    new Pared(465,200,1,170,7),
    new Pared(605,280,1,100,7),
      //mapa8
    new Pared(175,50,1,140,8),
    new Pared(175,280,1,140,8),
    new Pared(890,50,1,450,8),
    new Pared(0,190,1,70,8)
  ],

  mapas:[
    new Mapa('images/mapa/mapa1.png', 0, 1),
    new Mapa('images/mapa/mapa2.png', 1, 2),
    new Mapa('images/mapa/mapa4.png', 2, 3),
    new Mapa('images/mapa/mapa3.png', 3, 4),
    new Mapa('images/mapa/mapa4.png', 4, 5),
    new Mapa('images/mapa/mapa5.png', 5, 6),
    new Mapa('images/mapa/mapa6.png', 6, 7),
    new Mapa('images/mapa/mapa7.png', 7, 8)

  ],
};

Juego.iniciarRecursos = function() {
  Resources.load([
    'images/mapa/mapa1.png',
    'images/mapa/mapa2.png',
    'images/mapa/mapa3.png',
    'images/mapa/mapa4.png',
    'images/mapa/mapa5.png',
    'images/mapa/mapa6.png',
    'images/mapa/mapa7.png',
    'images/pj/magoAbajo.png',
    'images/pj/magoArriba.png',
    'images/pj/magoCaminar.png',
    'images/pj/guerreroCaminar1.png'

  ]);
  Resources.onReady(this.comenzar.bind(Juego));
};

$(document).ready(function(){
  if (player_selection()) {
    $('#seleccionDePersonaje').fadeOut(1000);
    console.log("se");
    Juego.iniciarRecursos();
    Juego.enableInputs();
    Juego.mapas.forEach(function(mapa){
      if (mapa.numeroMapa == Juego.mapaActual) {
        dibujarFondo(mapa.sprite);
        dibujarPersonaje(Juego.entidad);
      }
    });
  }
});

//camptura las teclas
Juego.enableInputs = function(){
    document.addEventListener('keydown', function(evt) { // Cuando se pulsa la tecla
        Juego.pressing[evt.keyCode] = true;
    });

    document.addEventListener('keyup', function(evt) { // Cuando se relaja la tecla
        Juego.pressing[evt.keyCode] = false;
    });
}

Juego.comenzar = function() {
};


Juego.resaltarSeccionMapa = function(numeroMapa) {
  switch (numeroMapa) {
    case 1:
      document.getElementById('mapaCompleto').src = "images/mapa/mapaSeccion1.png";
      break;
    case 2:
      document.getElementById('mapaCompleto').src = "images/mapa/mapaSeccion2.png";
      break;
    case 3:
      document.getElementById('mapaCompleto').src = "images/mapa/mapaSeccion3.png";
      break;
    case 4:
      document.getElementById('mapaCompleto').src = "images/mapa/mapaSeccion4.png";
      break;
    case 5:
      document.getElementById('mapaCompleto').src = "images/mapa/mapaSeccion3.png";
      break;
    case 6:
      document.getElementById('mapaCompleto').src = "images/mapa/mapaSeccion5.png";
      break;
    case 7:
      document.getElementById('mapaCompleto').src = "images/mapa/mapaSeccion6.png";
      break;
    case 8:
      document.getElementById('mapaCompleto').src = "images/mapa/mapaSeccion7.png";
      break;
    default:

  }
};

Juego.pasoPorLaPuerta = function(numeroPuerta) {
  for (var i = 0; i < this.puertas.length; i++) {
    if (i == numeroPuerta) {
      if (numeroPuerta == 2) {
        return((sprite.y) > this.puertas[i].posicionYA && (sprite.y) <
                this.puertas[i].posicionYB && (sprite.x) <
                this.puertas[i].posicionXA && (sprite.x) >
                this.puertas[i].posicionXB);
      }
      if (numeroPuerta == 5) {
        return((sprite.y) < this.puertas[i].posicionYA && (sprite.y) >
                this.puertas[i].posicionYB && (sprite.x) >
                this.puertas[i].posicionXA && (sprite.x) <
                this.puertas[i].posicionXB);
      }
      return((sprite.y) > this.puertas[i].posicionYA && (sprite.y) <
              this.puertas[i].posicionYB && (sprite.x) >
              this.puertas[i].posicionXA && (sprite.x) <
              this.puertas[i].posicionXB);
    }
  }
};

Juego.posicionarJugador = function(numeroMapa) {
switch (numeroMapa) {
  case 1:
    sprite.x = 71;
    sprite.y = 190;
    break;
  case 2:
    sprite.x = 10;
    break;
  case 3:
    sprite.y = 10;
    break;
  case 4:
    sprite.x = 850;
    break;
  case 5:
    sprite.x = 5;
    break;
  case 6:
    sprite.x = 5;
    break;
  case 7:
    sprite.y = 450;
    break;
  case 8:
    this.jugador.y = 5;
    break;
  default:

}
};

/* Aca se chequea si el jugador se peude mover a la posicion destino.
 Es decir, que no haya obstaculos que se interpongan. De ser asi, no podra moverse */
Juego.puedeMoverse = function(posicionJugadorX, posicionJugadorY) {
  var puedeMoverse = true
  this.paredes.forEach(function(pared) {
    if (pared.numeroMapa == this.mapaActual) {
      //no esta bien pero por el momento funciona
      if (this.pressing[this.KEY_LEFT]) {
        if (this.intersecan(pared, this.entidad, posicionJugadorX - 1, posicionJugadorY)) {
          puedeMoverse = false;
        }
      }
      if (this.pressing[this.KEY_RIGHT]) {
        if (this.intersecan(pared, this.entidad, posicionJugadorX + 1, posicionJugadorY)) {
          puedeMoverse = false;
        }
      }
      if (this.pressing[this.KEY_UP]) {
        if (this.intersecan(pared, this.entidad, posicionJugadorX, posicionJugadorY - 1)) {
          puedeMoverse = false;
        }
      }
      if (this.pressing[this.KEY_DOWN]) {
        if (this.intersecan(pared, this.entidad, posicionJugadorX, posicionJugadorY + 1)) {
          puedeMoverse = false;
        }
      }
    }
  }, this)
  return puedeMoverse
};

// /* Este metodo chequea si los elementos 1 y 2 si cruzan en x e y
//  x e y representan la coordenada a la cual se quiere mover el elemento2*/
Juego.intersecan = function(pared, jugador, posicionJugadorX, posicionJugadorY) {
  // console.log(posicionJugadorX);
  var izquierda1 = pared.x + 10;
  var derecha1 = izquierda1 + pared.ancho;
  var techo1 = pared.y + 10;
  var piso1 = techo1 + pared.alto;
  var izquierda2 = posicionJugadorX;
  var derecha2 = izquierda2 + jugador.frames.width;
  var techo2 = posicionJugadorY;
  var piso2 = techo2 + jugador.frames.height;

  return ((piso1 >= techo2) && (techo1 <= piso2) &&
    (derecha1 >= izquierda2) && (izquierda1 <= derecha2))
};
