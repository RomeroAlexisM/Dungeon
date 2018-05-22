 var servidor = 'http://127.0.0.1:5000';
function players() {

 axios.get(servidor + '/images/character-selection/').then(function(response) {
   // for (var i = 0; i < response.data.length; i++) {
        console.log(response.data);
   // }

   // $('#guerrero').append("Clase: "+response.data.playables_list[0].nombre+'<br>');
   //  $('#guerrero').append("Energia: "+response.data.playables_list[0].energia);
   // $('#mago').append("Clase: "+response.data.playables_list[1].nombre);
   //  $('#mago').append("     Energia: "+response.data.playables_list[1].energia);

 }).catch(function(error) {
 console.log(error);
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
