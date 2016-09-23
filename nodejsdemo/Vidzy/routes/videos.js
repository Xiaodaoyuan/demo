var express = require('express');
var router = express.Router();

var monk = require('monk');
var db = monk('localhost:27017/vidzy');

router.get('/',function(req,res){
	var collection = db.get('videos');
	collection.find({},function(err,data){
		if (err) throw err;
		res.json(data);
	});
});

module.exports = router;