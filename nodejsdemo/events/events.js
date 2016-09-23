var events = require('events')

var eventEmitter = new events.EventEmitter();

var connectHandler = function connected(){
	console.log('connect success....');
	eventEmitter.emit('recieve');
	eventEmitter.emit('recieve');
};

eventEmitter.on('connect',connectHandler);

eventEmitter.once('recieve',function(){
	console.log('recieve data success....');
});

eventEmitter.emit('connect');
eventEmitter.emit('connect');

