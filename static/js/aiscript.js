$(document).ready(function() {
	var number = parseInt($(document).find('#user').text(), 10);
	var maxTime = 1000;
	var id = setInterval(function() {updateAI()}, maxTime);

	$('#reset-model').click(function() {
		$.getJSON('/aireset', {user:number}, function(data) {processJSONresponse(data)});
	});

	 $('#super-slow').click(function() {
	 	console.log('slow');
	 	$.get('/set_speed', {speed: 'superslow', user:number}, function(data) {maxTime = data.speed; clearInterval(id);id=setInterval(function() {updateAI()}, maxTime);});
	 })
	 $('#slow').click(function() {
	 	$.get('/set_speed', {speed: 'slow', user:number}, function(data) {maxTime = data.speed; clearInterval(id);id=setInterval(function() {updateAI()}, maxTime);});
	 })
	 $('#mid').click(function() {
	 	$.get('/set_speed', {speed: 'mid', user:number}, function(data) {maxTime = data.speed; clearInterval(id);id=setInterval(function() {updateAI()}, maxTime);});
	 })
	 $('#fast').click(function() {
	 	$.get('/set_speed', {speed: 'fast', user:number}, function(data) {maxTime = data.speed; clearInterval(id);id=setInterval(function() {updateAI()}, maxTime);});
	 })
	 $('#super-fast').click(function() {
	 	$.get('/set_speed', {speed: 'superfast', user:number}, function(data) {maxTime = data.speed; clearInterval(id);id=setInterval(function() {updateAI()}, maxTime);});
	 })

	function updateAI() {
		$.getJSON('/aiupdate', {user:number}, function(data) {processJSONresponse(data)});
	}

	function processJSONresponse(data) {
		tilesArray = data.tiles;
		len = tilesArray.length;
		$pieces = $('#pieces');
		$pieces.html('');
		for (i=0; i<len; i++) {
			tempDict = tilesArray[i];
			row = tempDict.row;
			column = tempDict.column;
			tilevalue = tempDict.tilevalue;
			html = "<div class = 'row"+row+" column"+column+" value"+tilevalue+" tile' style='background-color:"+chooseTileColor(tilevalue)+"'>"+tilevalue+"</div>";
			$pieces.append(html);
		};
	};

	function chooseTileColor(value) {
		if (value == 2) {
			color = '#FFFFFF';
		};
		if (value == 4) {
			color = '#DDDDFF';
		};
		if (value == 8) {
			color = '#BBBBFF';
		};
		if (value == 16) {
			color = '#9999FF';
		};
		if (value == 32) {
			color = '#7777FF';
		};
		if (value == 64) {
			color = '#5555FF';
		};
		if (value == 128) {
			color = '#3333FF';
		};
		if (value == 256) {
			color = '#1111FF';
		};
		if (value == 512) {
			color = '#0000EE';
		};
		if (value == 1024) {
			color = '#0000CC';
		};
		if (value == 2048) {
			color = '#0000AA';
		};
		if (value == 4096) {
			color = '#000088';
		};
		if (value == 8192) {
			color = '#000066';
		};
		return color;
	};
});