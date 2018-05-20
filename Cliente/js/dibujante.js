var canvas = document.getElementById('canvas');
var stage = new createjs.Stage(canvas);
var sprite = "";
// var pressing= [];
// var KEY_LEFT= 37;
// var KEY_RIGHT=39;

function dibujarFondo(mapa){
  var bitmap = new createjs.Bitmap(mapa);
  stage.addChild(bitmap);
  stage.update();
};

function dibujarPersonaje(entidad){
  // enableInputs();
  var spriteSheet = new createjs.SpriteSheet(entidad);
  sprite = new createjs.Sprite(spriteSheet, "stand");

  sprite.moving = false;
  sprite.regX = sprite.getBounds().width / 2;
  sprite.regY = sprite.getBounds().height / 2;
    Juego.posicionarJugador(Juego.mapaActual);
  // sprite.x = canvas.width / 2;
  // sprite.y = canvas.height / 2;

  stage.addChild(sprite);

<<<<<<< HEAD
  createjs.Ticker.setFPS(60);
  createjs.Ticker.on("tick", Entidad.onTick, this);
};
=======
  /* Dibuja una entidad en el juego, esto puede ser el jugador, un enemigo, etc
   es decir, cualquiera objeto que separ responder a los mensajes: sprite, x, y, ancho y alto*/
  dibujarEnte: function (entidad) {
    this.dibujarImagen(entidad.sprite, entidad.x, entidad.y, entidad.ancho, entidad.alto);
  },

  /* Dibuja un rectangulo del color pasado por paramentro en la posicion x, y
   con ancho y alto*/
  dibujarRectangulo: function (color, x, y, ancho, alto) {
    var ctx = this.canvas.getContext('2d');
    ctx.fillStyle = color;
    ctx.fillRect(x, y, ancho, alto);
  },
}
>>>>>>> e3a543a51f8305a6042a298ed45aa79c3ea3a335
