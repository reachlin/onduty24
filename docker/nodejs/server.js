'use strict';

const express = require('express');
const marked = require('marked');
const fs = require('fs');
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

app.get('/containers_bss_health_check', function(req, res){
  res.render('containers_bss_health_check', {name: 'containers_bss_health_check'});
});

app.get('/action/containers_bss_health_check', function(req, res){
  var path = __dirname + "/documentation-pages/docs/runbooks/containers_bss_health_check.md";
  var md = fs.readFileSync(path, 'utf8');
  var render = new marked.Renderer();
  var line = 0;
  render.html = function(text){
    var rtn = "<script>alert('enabled');</script>"+text;
    return rtn;
  };
  render.paragraph = function(text){
    var rtn = text + "[XXX]"+line;
    line++;
    return rtn;
  };
  var html = marked(md, {renderer: render});
  res.send(html);
});

app.listen(PORT);
console.log('Running on http://localhost:' + PORT);

