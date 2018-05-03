/* El objeto jugador es un objeto literal que se encuentra incompleto.
 Solo tiene asignadas algunas de sus propiedades y ningun metodo */
var Jugador = function(sprite, x, y, ancho, alto){
  /* el sprite contiene la ruta de la imagen
  */
  this.sprite = sprite;
 this.x = x;
 this.y = y;
 this.ancho = ancho;
 this.alto = alto;
}

  Jugador.prototype.mover = function(tecla){

    switch (tecla) {
      case 'izq':
      this.x = this.x - 10;
      break;
      case 'arriba':
      this.y = this.y - 10;
      break;
      case 'der':
      this.x = this.x + 10;
      break;
      case 'abajo':
      this.y = this.y + 10;
      break;
    }
  };

  Jugador.prototype.posicionar = function() {

  }
