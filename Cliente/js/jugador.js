/* El objeto jugador es un objeto literal que se encuentra incompleto.
 Solo tiene asignadas algunas de sus propiedades y ningun metodo */
var Jugador = {
  /* el sprite contiene la ruta de la imagen
  */
  sprite: 'images/jugador1.png',
  x: 131,
  y: 270,
  ancho: 15,
  alto: 30,
  velocidad: 10,
  vidas: 5,

  mover(tecla){
    switch (tecla) {
      case 'izq':
      this.x = this.x - 10;
      this.sprite= 'images/jugador1.png';
      this.ancho= 30;
      this.alto= 15;
      break;
      case 'arriba':
      this.y = this.y - 10;
      this.sprite= 'images/jugador1.png';
      this.ancho= 15;
      this.alto= 30;
      break;
      case 'der':
      this.x = this.x + 10;
      this.sprite= 'images/jugador1.png';
      this.ancho= 30;
      this.alto= 15;
      break;
      case 'abajo':
      this.y = this.y + 10;
      this.sprite= 'images/jugador1.png';
      this.ancho= 15;
      this.alto= 30;
      break;
    }
  },

  // perderVidas(cantVidas){
  //   this.vidas = this.vidas - cantVidas;
  // },
}
