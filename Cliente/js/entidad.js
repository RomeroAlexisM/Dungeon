/* El objeto jugador es un objeto literal que se encuentra incompleto.
 Solo tiene asignadas algunas de sus propiedades y ningun metodo */
var Entidad = function(framerate, images, frames, animations){
  this.framerate = framerate;
  this.images = images;
  this.frames = frames;
  this.animations = animations;
}

//Anima el movimiento del personaje
Entidad.onTick = function(e){
  if(!e.paused){
       if(Juego.pressing[Juego.KEY_LEFT]){
        if (Juego.puedeMoverse(sprite.x, sprite.y)) {
          sprite.x--;
        }
          if(!sprite.moving){
             sprite.gotoAndPlay('run');
             sprite.setTransform (sprite.x, sprite.y, 1, 1, 0, 0, 0, sprite.regX, sprite.regY); // setTransform con valores invariantes
           }
          sprite.moving = true;
       }
       if(Juego.pressing[Juego.KEY_RIGHT]){
         if (Juego.puedeMoverse(sprite.x, sprite.y)) {
           sprite.x++;
         }
           if(!sprite.moving){
             sprite.gotoAndPlay('run');
             sprite.setTransform (sprite.x, sprite.y, -1, 1, 0, 0, 0, sprite.regX, sprite.regY); // setTransform con un -1 en scaleX para hacer el 'flip'
           }
          sprite.moving = true;

        }
       if(!Juego.pressing[Juego.KEY_LEFT] && !Juego.pressing[Juego.KEY_RIGHT]){ // Si no se presiona ninguna de estas teclas, llamamos a 'idle'
           if(sprite.moving){
           sprite.gotoAndPlay('stand');
           }
           sprite.moving = false;
       }
       if(Juego.pressing[Juego.KEY_UP]){
        if (Juego.puedeMoverse(sprite.x, sprite.y)) {
          sprite.y--;
        }
          if(!sprite.moving){
             sprite.gotoAndPlay('up');
             sprite.setTransform (sprite.x, sprite.y, 1, 1, 0, 0, 0, sprite.regX, sprite.regY); // setTransform con valores invariantes
           }
          sprite.moving = true;
       }
       if(Juego.pressing[Juego.KEY_DOWN]){
        if (Juego.puedeMoverse(sprite.x, sprite.y)) {
          sprite.y++;
        }
          if(!sprite.moving){
             sprite.gotoAndPlay('down');
             sprite.setTransform (sprite.x, sprite.y, 1, 1, 0, 0, 0, sprite.regX, sprite.regY); // setTransform con valores invariantes
           }
          sprite.moving = true;
       }
       stage.update(e);
  }
};
