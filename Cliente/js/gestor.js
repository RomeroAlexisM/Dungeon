function peticionGet() {

 axios.get('/telefonos').then(function(response) {
 console.log(response.data);
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
