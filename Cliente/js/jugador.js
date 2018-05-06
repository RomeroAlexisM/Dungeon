/* El objeto jugador es un objeto literal que se encuentra incompleto.
 Solo tiene asignadas algunas de sus propiedades y ningun metodo */
var Jugador = function(sprite, x, y, ancho, alto, velocidad,pasos){
  /* el sprite contiene la ruta de la imagen
  */
  this.sprite = sprite;
 this.x = x;
 this.y = y;
 this.ancho = ancho;
 this.alto = alto;
 this.velocidad = velocidad;
 this.pasos = pasos;
}

  Jugador.prototype.mover = function(tecla){
    switch (tecla) {
      case 'izq':
      if (this.pasos == 1) {
        this.sprite = 'images/pj/magoIzquierdaPaso1.png';
        this.pasos++;
      }else if (this.pasos == 2) {
        this.sprite = 'images/pj/magoIzquierdaPaso2.png';
        this.pasos++;
      }
      else if (this.pasos == 3) {
        this.sprite = 'images/pj/magoIzquierdaPaso3.png';
        this.pasos++;
      }
      else if (this.pasos == 4) {
        this.sprite = 'images/pj/magoIzquierdaPaso4.png';
        this.pasos++;
      }
      else if (this.pasos == 5) {
        this.sprite = 'images/pj/magoIzquierdaPaso5.png';
        this.pasos = 1;
      }
      this.x = this.x - 4;
      break;
      case 'arriba':
      this.y = this.y - 4;
      this.sprite = 'images/pj/magoArriba.png';
      break;
      case 'der':
      if (this.pasos == 1) {
        this.sprite = 'images/pj/magoDerechaPaso1.png';
        this.pasos++;
      }else if (this.pasos == 2) {
        this.sprite = 'images/pj/magoDerechaPaso2.png';
        this.pasos++;
      }
      else if (this.pasos == 3) {
        this.sprite = 'images/pj/magoDerechaPaso3.png';
        this.pasos++;
      }
      else if (this.pasos == 4) {
        this.sprite = 'images/pj/magoDerechaPaso4.png';
        this.pasos++;
      }
      else if (this.pasos == 5) {
        this.sprite = 'images/pj/magoDerechaPaso5.png';
        this.pasos = 1;
      }
      this.x = this.x + 4;
      // this.sprite = 'images/pj/magoDerecha.png';
      break;
      case 'abajo':
      this.y = this.y + 4;
      this.sprite = 'images/pj/magoAbajo.png';
      break;
    }
  };

  Jugador.prototype.posicionar = function() {

  }
