/* El objeto jugador es un objeto literal que se encuentra incompleto.
 Solo tiene asignadas algunas de sus propiedades y ningun metodo */
var Jugador = function(sprite, x, y, ancho, alto, velocidad, pasos, direccion){
  /* el sprite contiene la ruta de la imagen
  */
  this.sprite = sprite;
 this.x = x;
 this.y = y;
 this.ancho = ancho;
 this.alto = alto;
 this.velocidad = velocidad;
 this.pasos = pasos;
 this.direccion = direccion;
}

  Jugador.prototype.mover = function(tecla){
    var posicion = '';
    switch (tecla) {
      case 'izq':
      this.direccion = 'izquierda';
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
      this.direccion = 'arriba';
      this.y = this.y - 4;
      this.sprite = 'images/pj/magoArriba.png';
      break;
      case 'der':
      this.direccion = 'derecha';
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
      console.log(posicion);
      this.x = this.x + 4;
      // this.sprite = 'images/pj/magoDerecha.png';
      break;
      case 'abajo':
      this.direccion = 'abajo';
      this.y = this.y + 4;
      this.sprite = 'images/pj/magoAbajo.png';
      break;
      case 'ataque1':
        if (this.direccion == 'derecha') {
          this.sprite = 'images/pj/magoAtaque1Derecha.png';
          console.log(posicion);
          this.volverAposicionAnterior(posicion);
        }else if (this.direccion == 'izquierda') {
          this.sprite = 'images/pj/magoAtaque1Izquierda.png';
          this.volverAposicionAnterior(posicion);
        }else if (this.direccion == 'arriba') {
          this.sprite = 'images/pj/magoAtaque1Arriba.png';
          this.volverAposicionAnterior(posicion);
        }
        else if (this.direccion == 'abajo') {
          this.sprite = 'images/pj/magoAtaque1Abajo.png';
          this.volverAposicionAnterior(posicion);
        }
      break;
      case 'ataque2':
        if (this.direccion == 'derecha') {
          this.sprite = 'images/pj/magoAtaque2Derecha.png';
          this.volverAposicionAnterior(posicion);
        }else if (this.direccion == 'izquierda') {
          this.sprite = 'images/pj/magoAtaque2Izquierda.png';
          this.volverAposicionAnterior(posicion);
        }
      break;
    }
  };

  Jugador.prototype.volverAposicionAnterior = function(posicion) {
   setTimeout(function(){
     console.log("cambio");
     this.sprite = posicion;
     console.log(posicion);
   },2000);
  }
