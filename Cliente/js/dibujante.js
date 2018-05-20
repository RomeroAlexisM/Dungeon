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

  createjs.Ticker.setFPS(60);
  createjs.Ticker.on("tick", Entidad.onTick, this);
};
