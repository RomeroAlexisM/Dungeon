var Juego = {
  //configuracion de tamaño de mapa

  ancho: 900,
  alto: 500,
  mapaActual: 0,

  jugador: new Jugador( 'images/jugador1.png',71,190,15,30),

  puerta:[
    new Puerta(890,895,360,420),
    new Puerta(110,240,470,490),
    new Puerta(0,-20,10,90),
    new Puerta(885,900,170,480),
    new Puerta(885,900,170,480),
    new Puerta(345,735,0,-20),
    new Puerta(885,900,200,270)
  ],

  mapa:[
    new Mapa('images/mapa1.png', 0, 1),
    new Mapa('images/mapa2.png', 1, 2),
    new Mapa('images/mapa4.png', 2, 3),
    new Mapa('images/mapa3.png', 3, 4),
    new Mapa('images/mapa4.png', 4, 5),
    new Mapa('images/mapa5.png', 5, 6),
    new Mapa('images/mapa6.png', 6, 7),
    new Mapa('images/mapa7.png', 7, 8)

  ]
}

Juego.iniciarRecursos = function() {
  Resources.load([
    'images/mapa1.png',
    'images/mapa2.png',
    'images/mapa3.png',
    'images/mapa4.png',
    'images/mapa5.png',
    'images/mapa6.png',
    'images/mapa7.png',
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
  this.jugador.mover(tecla);
  // // Si se puede mover hacia esa posicion hay que hacer efectivo este movimiento
  // if (this.chequearColisiones(movX + this.jugador.x, movY + this.jugador.y)) {
  //
  //
  // }
};

Juego.dibujar = function() {
  for (var i = 0; i < this.mapa.length; i++) {
    if (this.pasoPorLaPuerta(this.mapa[i].numeroPuerta)) {
      // Borrar el fotograma actual
      Dibujante.borrarAreaDeJuego();
      //Se pinta la imagen de fondo segun el estado del juego
      this.dibujarFondo(this.mapa[i+1].sprite);
      this.posicionarJugador(this.mapa[i+1].numeroMapa);
      Dibujante.dibujarEntidad(this.jugador);
      this.mapaActual++;

    }else {
      if (i == this.mapaActual) {
        Dibujante.borrarAreaDeJuego();
        this.resaltarSeccionMapa(this.mapa[i].numeroMapa);
        this.dibujarFondo(this.mapa[i].sprite);
        Dibujante.dibujarEntidad(this.jugador);

      }
    }
  };

  // this.dibujarFondo();

};

Juego.resaltarSeccionMapa = function(numeroMapa) {
  console.log(numeroMapa);
  switch (numeroMapa) {
    case 1:
      document.getElementById('mapaCompleto').src = "images/mapaSeccion1.png";
      break;
    case 2:
      document.getElementById('mapaCompleto').src = "images/mapaSeccion2.png";
      break;
    case 3:
      document.getElementById('mapaCompleto').src = "images/mapaSeccion3.png";
      break;
    case 4:
      document.getElementById('mapaCompleto').src = "images/mapaSeccion4.png";
      break;
    case 5:
      document.getElementById('mapaCompleto').src = "images/mapaSeccion3.png";
      break;
    case 6:
      document.getElementById('mapaCompleto').src = "images/mapaSeccion5.png";
      break;
    case 7:
      document.getElementById('mapaCompleto').src = "images/mapaSeccion6.png";
      break;
    case 8:
      document.getElementById('mapaCompleto').src = "images/mapaSeccion7.png";
      break;
    default:

  }
};

Juego.pasoPorLaPuerta = function(numeroPuerta) {
  for (var i = 0; i < this.puerta.length; i++) {
    if (i == numeroPuerta) {
      if (numeroPuerta == 2) {
        return((this.jugador.y) > this.puerta[i].posicionYA && (this.jugador.y) <
                this.puerta[i].posicionYB && (this.jugador.x) <
                this.puerta[i].posicionXA && (this.jugador.x) >
                this.puerta[i].posicionXB);
      }
      if (numeroPuerta == 5) {
        return((this.jugador.y) < this.puerta[i].posicionYA && (this.jugador.y) >
                this.puerta[i].posicionYB && (this.jugador.x) >
                this.puerta[i].posicionXA && (this.jugador.x) <
                this.puerta[i].posicionXB);
      }
      return((this.jugador.y) > this.puerta[i].posicionYA && (this.jugador.y) <
              this.puerta[i].posicionYB && (this.jugador.x) >
              this.puerta[i].posicionXA && (this.jugador.x) <
              this.puerta[i].posicionXB);
    }
  }
};

Juego.posicionarJugador = function(numeroMapa) {
  console.log(numeroMapa);
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
    this.jugador.x = 871;
    break;
  case 5:
    this.jugador.x = 5;
    break;
  case 6:
    this.jugador.x = 5;
    break;
  case 7:
    this.jugador.y = 490;
    break;
  case 8:
    this.jugador.y = 5;
    break;
  default:

}
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
    40: 'abajo'
  };

  Juego.capturarMovimiento(allowedKeys[e.keyCode]);
});
