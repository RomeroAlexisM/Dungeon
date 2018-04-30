var Juego = {
  //configuracion de tamaño de mapa
  ancho: 740,
  alto: 684
}

Juego.iniciarRecursos = function() {
  Resources.load([
    'images/mapa1.png',
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
  // this.calcularAtaques();
  // this.moverEnemigos();
}

// Captura las teclas y si coincide con alguna de las flechas tiene que
// hacer que el jugador principal se mueva
Juego.capturarMovimiento = function(tecla) {
  // var movX = 0;
  // var movY = 0;
  // var velocidad = this.jugador.velocidad;
Jugador.mover(tecla);
  // // El movimiento esta determinado por la velocidad del jugador
  // if (tecla == 'izq') {
  //   movX = -velocidad;
  // }
  // if (tecla == 'arriba') {
  //   movY = -velocidad;
  // }
  // if (tecla == 'der') {
  //   movX = velocidad;
  // }
  // if (tecla == 'abajo') {
  //   movY = velocidad;
  // }
  //
  // // Si se puede mover hacia esa posicion hay que hacer efectivo este movimiento
  // if (this.chequearColisiones(movX + this.jugador.x, movY + this.jugador.y)) {
  //
  //
  // }
};

Juego.dibujar = function() {
  // Borrar el fotograma actual
  Dibujante.borrarAreaDeJuego();
  //Se pinta la imagen de fondo segun el estado del juego
  this.dibujarFondo();

  Dibujante.dibujarEntidad(Jugador);

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


};

/* Recorre los enemigos haciendo que se muevan. De la misma forma que hicimos
un recorrido por los enemigos para dibujarlos en pantalla ahora habra que hacer
una funcionalidad similar pero para que se muevan.*/
// Juego.moverEnemigos = function() {
//   this.enemigos.forEach(function(enemigo){
//     enemigo.mover();
//   });
// };

Juego.dibujarFondo = function() {
  Dibujante.dibujarImagen('images/mapa1.png', 0, 5, this.ancho, this.alto);
  // // Si se termino el juego hay que mostrar el mensaje de game over de fondo
  // if (this.terminoJuego()) {
  //   Dibujante.dibujarImagen('imagenes/mensaje_gameover.png', 0, 5, this.anchoCanvas, this.altoCanvas);
  //   document.getElementById('reiniciar').style.visibility = 'visible';
  //   Dibujante.dibujarEntidad(null);
  // }
// Si se gano el juego hay que mostrar el mensaje de ganoJuego de fondo
//   else if (this.ganoJuego()) {
//     Dibujante.dibujarImagen('imagenes/Splash.png', 190, 113, 500, 203);
//     document.getElementById('reiniciar').style.visibility = 'visible';
//     Dibujante.dibujarEntidad(null);
//   } else {
//     Dibujante.dibujarImagen('imagenes/mapa.png', 0, 5, this.anchoCanvas, this.altoCanvas);
//   }
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
