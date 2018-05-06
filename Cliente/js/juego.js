var Juego = {
  //configuracion de tamaño de mapa

  ancho: 900,
  alto: 500,
  mapaActual: 0,

  jugador: new Jugador('images/pj/magoDerecha.png',71,190,25,40,10,1,'derecha'),

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
    new Pared(190,80,680,1,0),
    new Pared(190,490,680,1,0),
    new Pared(0,160,190,1,0),
    new Pared(0,250,190,1,0),
    new Pared(871,360,30,1,0),
    new Pared(871,450,30,1,0),
      //mapa2
    new Pared(0,360,240,1,1),
    new Pared(0,450,100,1,1),
      //mapa3
    new Pared(0,10,100,1,2),
    new Pared(0,100,240,1,2),
    new Pared(110,0,120,1,2),
      //mapa4
    new Pared(191,10,710,1,3),
    new Pared(401,100,499,1,3),
    new Pared(301,120,180,1,3),
    new Pared(401,250,68,1,3),
    new Pared(401,290,130,1,3),
    new Pared(191,370,340,1,3),
    new Pared(531,170,369,1,3),
    new Pared(531,490,369,1,3),
      //mapa5
    new Pared(0,170,900,1,4),
    new Pared(0,490,900,1,4),
      //mapa6
    new Pared(0,170,345,1,5),
    new Pared(0,490,345,1,5),
    new Pared(345,290,130,1,5),
    new Pared(345,370,270,1,5),
    new Pared(615,130,130,1,5),
    new Pared(340,130,145,1,5),
      //mapa7
    new Pared(335,370,140,1,6),
    new Pared(495,190,425,1,6),
    new Pared(605,380,140,1,6),
    new Pared(605,270,295,1,6),
    new Pared(345,500,380,1,6),
      //mapa8
    new Pared(0,190,185,1,7),
    new Pared(0,270,185,1,7),
    new Pared(185,40,700,1,7),
    new Pared(185,430,700,1,7),


    //verticales
      //mapa1
    new Pared(1,170,1,60,0),
    new Pared(199,250,1,240,0),
    new Pared(199,90,1,70,0),
    new Pared(871,450,1,40,0),
    new Pared(871,90,1,280,0),
    new Pared(0,370,1,50,1),
      //mapa2
    new Pared(250,370,1,130,1),
    new Pared(100,450,1,50,1),
      //mapa3
    new Pared(250,0,1,100,2),
      //mapa4
    new Pared(201,0,3,380,3),
    new Pared(301,120,1,140,3),
    new Pared(471,120,1,140,3),
    new Pared(531,170,1,120,3),
    new Pared(531,370,1,120,3),
    new Pared(891,0,1,100,3),
     //mapa5
    new Pared(0,150,1,350,4),
     //mapa6
    new Pared(350,170,1,120,5),
    new Pared(350,370,1,120,5),
    new Pared(615,130,1,240,5),
    new Pared(480,130,1,160,5),
    new Pared(335,0,1,130,5),
    new Pared(750,0,1,130,5),
    new Pared(0,150,1,350,5),
      //mapa7
    new Pared(335,390,1,110,6),
    new Pared(745,380,1,120,6),
    new Pared(465,200,1,170,6),
    new Pared(605,280,1,100,6),
      //mapa8
    new Pared(175,50,1,140,7),
    new Pared(175,280,1,140,7),
    new Pared(890,50,1,450,7),
    new Pared(0,190,1,70,7)
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

  ]
}

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
    'images/pj/magoDerecha.png',
    'images/pj/magoIzquierda.png',
    'images/pj/magoIzquierdaPaso1.png',
    'images/pj/magoIzquierdaPaso2.png',
    'images/pj/magoIzquierdaPaso3.png',
    'images/pj/magoIzquierdaPaso4.png',
    'images/pj/magoIzquierdaPaso5.png',
    'images/pj/magoDerechaPaso1.png',
    'images/pj/magoDerechaPaso2.png',
    'images/pj/magoDerechaPaso3.png',
    'images/pj/magoDerechaPaso4.png',
    'images/pj/magoDerechaPaso5.png',
    'images/pj/magoAtaque1Izquierda.png',
    'images/pj/magoAtaque1Derecha.png',
    'images/pj/magoAtaque2Izquierda.png',
    'images/pj/magoAtaque2Derecha.png',
    'images/pj/magoAtaque1Arriba.png',
    'images/pj/magoAtaque1Abajo.png',

    'images/jugador1.png'
  ]);
  Resources.onReady(this.comenzar.bind(Juego));
};

Juego.comenzar = function() {
  // Inicializar el canvas del juego
  Dibujante.inicializarCanvas(this.ancho, this.alto);
  /* El bucle principal del juego se llamara continuamente para actualizar
  los movimientos y el pintado de la pantalla.*/
  this.buclePrincipal();
};

Juego.buclePrincipal = function() {
  // Con update se actualiza la logica del juego, tanto ataques como movimientos
  this.update();
  // Funcion que dibuja por cada fotograma a los objetos en pantalla.
  this.dibujar();
  // Esto es una forma de llamar a la funcion Juego.buclePrincipal() repetidas veces
  window.requestAnimationFrame(this.buclePrincipal.bind(this));
};

Juego.update = function() {
  // console.log("x: "+this.jugador.x+" y:"+this.jugador.y)
  // this.calcularAtaques();
  // this.moverEnemigos();
}

// Captura las teclas y si coincide con alguna de las flechas tiene que
// hacer que el jugador principal se mueva
Juego.capturarMovimiento = function(tecla) {
  var movX = 0;
  var movY = 0;
  var velocidad = this.jugador.velocidad;
  // El movimiento esta determinado por la velocidad del jugador
  if (tecla == 'izq') {
    movX = -velocidad;
  }
  if (tecla == 'arriba') {
    movY = -velocidad;
  }
  if (tecla == 'der') {
    movX = velocidad;
  }
  if (tecla == 'abajo') {
    movY = velocidad;
  }

  // Si se puede mover hacia esa posicion hay que hacer efectivo este movimiento
  if (this.puedeMoverse(movX + this.jugador.x, movY + this.jugador.y)) {
  this.jugador.mover(tecla);

  }
};

Juego.dibujar = function() {
  for (var i = 0; i < this.mapas.length; i++) {
    if (this.pasoPorLaPuerta(this.mapas[i].numeroPuerta)) {
      // Borrar el fotograma actual
      Dibujante.borrarAreaDeJuego();
      //Se pinta la imagen de fondo segun el estado del juego
      this.dibujarFondo(this.mapas[i+1].sprite);
      this.posicionarJugador(this.mapas[i+1].numeroMapa);
      Dibujante.dibujarEntidad(this.jugador);
      this.mapaActual++;

    }else {
      if (i == this.mapaActual) {
        Dibujante.borrarAreaDeJuego();
        this.resaltarSeccionMapa(this.mapas[i].numeroMapa);
        this.dibujarFondo(this.mapas[i].sprite);
        Dibujante.dibujarEntidad(this.jugador);

      }
    }
  };
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
        return((this.jugador.y) > this.puertas[i].posicionYA && (this.jugador.y) <
                this.puertas[i].posicionYB && (this.jugador.x) <
                this.puertas[i].posicionXA && (this.jugador.x) >
                this.puertas[i].posicionXB);
      }
      if (numeroPuerta == 5) {
        return((this.jugador.y) < this.puertas[i].posicionYA && (this.jugador.y) >
                this.puertas[i].posicionYB && (this.jugador.x) >
                this.puertas[i].posicionXA && (this.jugador.x) <
                this.puertas[i].posicionXB);
      }
      return((this.jugador.y) > this.puertas[i].posicionYA && (this.jugador.y) <
              this.puertas[i].posicionYB && (this.jugador.x) >
              this.puertas[i].posicionXA && (this.jugador.x) <
              this.puertas[i].posicionXB);
    }
  }
};

Juego.posicionarJugador = function(numeroMapa) {
switch (numeroMapa) {
  case 1:
    this.jugador.x = 71;
    this.jugador.y = 190;
    break;
  case 2:
    this.jugador.x = 10;
    break;
  case 3:
    this.jugador.y = 10;
    break;
  case 4:
    this.jugador.x = 850;
    break;
  case 5:
    this.jugador.x = 5;
    break;
  case 6:
    this.jugador.x = 5;
    break;
  case 7:
    this.jugador.y = 450;
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
      if (this.intersecan(pared, this.jugador, posicionJugadorX, posicionJugadorY)) {
        puedeMoverse = false
      }
    }
  }, this)
  return puedeMoverse
};

/* Este metodo chequea si los elementos 1 y 2 si cruzan en x e y
 x e y representan la coordenada a la cual se quiere mover el elemento2*/
Juego.intersecan = function(elemento1, elemento2, posicionJugadorX, posicionJugadorY) {
  var izquierda1 = elemento1.x -10;
  var derecha1 = izquierda1 + elemento1.ancho;
  var techo1 = elemento1.y - 10;
  var piso1 = techo1 + elemento1.alto;
  var izquierda2 = posicionJugadorX;
  var derecha2 = izquierda2 + elemento2.ancho;
  var techo2 = posicionJugadorY;
  var piso2 = techo2 + elemento2.alto;

  return ((piso1 >= techo2) && (techo1 <= piso2) &&
    (derecha1 >= izquierda2) && (izquierda1 <= derecha2))
};

Juego.dibujarFondo = function(url) {
  Dibujante.dibujarImagen(url, 0, 0, this.ancho, this.alto);

};

Juego.iniciarRecursos();

// Activa las lecturas del teclado al presionar teclas
// Documentacion: https://developer.mozilla.org/es/docs/Web/API/EventTarget/addEventListener
document.addEventListener('keydown', function(e) {
  var allowedKeys = {
    37: 'izq',
    38: 'arriba',
    39: 'der',
    40: 'abajo',
    65: 'ataque1',
    83: 'ataque2'
  };

  Juego.capturarMovimiento(allowedKeys[e.keyCode]);
});
