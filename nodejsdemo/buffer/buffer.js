var buf = new Buffer('xiaody');
console.log(buf.toString());

var buf1 = new Buffer(5);
buf1.write('xiaody');
console.log(buf1.toString());

var buf2 = new Buffer('xiaody1234');
console.log(buf2.toString('hex'));

console.log(buf2.length);
console.log(buf.toString('ascii',0,4));