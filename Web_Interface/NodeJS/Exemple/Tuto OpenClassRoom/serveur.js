var express = require('express');

var app = express();

/*app.get('/compter/:nombre', function(req, res) {
  var noms = ['Robert', 'Jacques', 'David'];
  res.render('page.ejs', {compteur: req.params.nombre, noms: noms});
});*/

app.get('/', function(req, res) {
  var system_time = "12h13";
  res.render('index.ejs', {system_time: system_time});
});

app.listen(8080);