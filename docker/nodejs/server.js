'use strict';

const express = require('express');

// Constants
const PORT = 8080;

const Emb = require('express-markdown-browser');
const emb = new Emb({path: __dirname + "/documentation-pages/docs"});

// App
const app = express();

app.set('view engine', 'jade');
app.set('views', 'views');
app.use(express.static('public'));


app.get('/', function (req, res) {
  res.send('Hello world\n');
});

app.get('/runbooks', emb, function(req, res, next) {console.log(res);next();});

/*
app.get('/ping', function(req, res) {
  var Ansible = require('node-ansible');
  var cmd = new Ansible.AdHoc().module('ping').hosts('all').user('ubuntu');
  var rtn = cmd.exec();
  rtn.then(function(msg){res.send(msg);}, function(error){res.send(error);});
});
*/


app.get('/action/containers_bss_health_check', function(req, res){
  res.render('containers_bss_health_check');
});

app.listen(PORT);
console.log('Running on http://localhost:' + PORT);

