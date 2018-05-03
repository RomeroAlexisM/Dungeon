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
  // // Borrar el fotograma actual
  // Dibujante.borrarAreaDeJuego();
  // //Se pinta la imagen de fondo segun el estado del juego
  // console.log(this.mapa);
  for (var i = 0; i < this.mapa.length; i++) {
    if ((this.jugador.y) < this.mapa[i].puertaSalidaYB && (this.jugador.y) > this.mapa[i].puertaSalidaYA && (this.jugador.x) == this.mapa[i].puertaSalidaX) {
        Dibujante.borrarAreaDeJuego();
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

  // Se recorren los obstaculos de la carretera pintandolos
  // this.obstaculosCarretera.forEach(function(obstaculo) {
  //   Dibujante.dibujarEntidad(obstaculo);
  // });

  // Se recorren los enemigos pintandolos
  // this.enemigos.forEach(function(enemigo) {
  //   Dibujante.dibujarEntidad(enemigo);
  // });

  // El dibujante dibuja las vidas del jugador
  // var tamanio = this.anchoCanvas / this.vidasInicial;
  // Dibujante.dibujarRectangulo('white', 0, 0, this.anchoCanvas, 8);
  // for (var i = 0; i < this.jugador.vidas; i++) {
  //   var x = tamanio * i
  //   Dibujante.dibujarRectangulo('red', x, 0, tamanio, 8);
  // }
  //El dibujante dibuja la linea de llegada
  Dibujante.dibujarRectangulo('blue', 1340, 463, 30, 100);

};

/* Recorre los enemigos haciendo que se muevan. De la misma forma que hicimos
un recorrido por los enemigos para dibujarlos en pantalla ahora habra que hacer
una funcionalidad similar pero para que se muevan.*/
// Juego.moverEnemigos = function() {
//   this.enemigos.forEach(function(enemigo){
//     enemigo.mover();
//   });
// };

Juego.dibujarFondo = function(url) {
  Dibujante.dibujarImagen(url, 0, 0, this.ancho, this.alto);

};

Juego.cambiarMapa = function() {
  if ((this.jugador.y) < 420 && (this.jugador.y) > 360 && (this.jugador.x) == 891) {
      Dibujante.borrarAreaDeJuego();
      this.dibujarFondo('images/mapa2.png');
      this.jugador.x = 10;
      Dibujante.dibujarEntidad(this.jugador);
  }
};

Juego.mapaIncial = function() {
  this.dibujarFondo('images/mapa1.png');
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
