var fs = require('fs');

var data = fs.readFile('input.txt',function(err,data){
	if(err){
		console.error(err);
		return;
	}
	console.log(data.toString());
});
console.log('end.....');