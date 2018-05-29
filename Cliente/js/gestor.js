 var servidor = 'http://127.0.0.1:5000';
 //muestra todos los personajes para seleccionar
function player_selection() {

 axios.get(servidor + '/images/character-selection/').then(function(response) {
   var personajes = response.data.character_list
   var cantidad = response.data.character_list.length;
   for (var i = 0; i <cantidad; i++) {
     //se clona un elemento que funciona como ejemplo de como se van a mostrar los personajes por pantalla
     var personaje = $(".ejemplo").clone();
     //se cargan los datos de las películas
     personaje.find(".imagen").attr("src", personajes[i].url);
     personaje.attr("id", personajes[i].id);
     //se agrega el personaje que al contenedor de personaje
     personaje.appendTo($(".contenedor"));
     //este personaje no va a ser mas de la clase ejemplo
     personaje.removeClass("ejemplo");
     //se muestra el personaje que se creo
     personaje.show();

     personaje.click(function() {
      var id = $(this).attr('id');
      console.log(id);
      return true;
     });
   }
 }).catch(function(error) {
 console.log(error);
 return false;
 });
 }


 function peticionPut() {

 axios.put('/telefonos/iphone', {
 nombre: "iphone",
 precio: "900"
 })
 .then(function(response) {
 console.log(response.data);
 })
 .catch(function(error) {
 console.log(error);
 });
 }
