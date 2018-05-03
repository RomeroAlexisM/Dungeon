var Juego = {
  //configuracion de tamaño de mapa

  ancho: 900,
  alto: 500,

  jugador: new Jugador( 'images/jugador1.png',131,270,15,30),

  mapa:[
    new Mapa('images/mapa1.png',0,0,0,891,360,420),
    new Mapa('images/mapa2.png',891,360,420,0,0,0)
  ]
}

Juego.iniciarRecursos = function() {
  Resources.load([
    'images/mapa1.png',
    'images/mapa2.png',
    'images/mapa3.png',
    'images/mapa4.png',
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
    if (this.estaEnLaPuerta(this.mapa[i])) {
      // Borrar el fotograma actual
        Dibujante.borrarAreaDeJuego();
        //Se pinta la imagen de fondo segun el estado del juego
        this.dibujarFondo(this.mapa[i+1].sprite);
        console.log(this.mapa[i+1].sprite);
        // this.jugador.x = 10;
    }else {
        Dibujante.borrarAreaDeJuego();
        this.dibujarFondo(this.mapa[0].sprite);
        console.log("se");
    }
  };

  // this.dibujarFondo();
  Dibujante.dibujarEntidad(this.jugador);
};

Juego.estaEnLaPuerta = function(mapa) {
  return ((this.jugador.y) < mapa.puertaSalidaYB && (this.jugador.y) >
          mapa.puertaSalidaYA && (this.jugador.x) == mapa.puertaSalidaX);
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
