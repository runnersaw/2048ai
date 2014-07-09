$(document).ready(function() {
	var number = parseInt($(document).find('#user').text(), 10);

	$('#reset-model').click(function() {
		$.getJSON('/selfreset', {user:number}, function(data) {processJSONresponse(data);});
	});

	$(document).keydown(function(e){
		if (e.keyCode == 37) {
			$.getJSON('/selfupdate', {user:number, direction:'left'}, function(data) {processJSONresponse(data);});
		}
		if (e.keyCode == 38) {
			$.getJSON('/selfupdate', {user:number, direction:'up'}, function(data) {processJSONresponse(data);});
		}
		if (e.keyCode == 39) {
			$.getJSON('/selfupdate', {user:number, direction:'right'}, function(data) {processJSONresponse(data);});
		}
		if (e.keyCode == 40) {
			$.getJSON('/selfupdate', {user:number, direction:'down'}, function(data) {processJSONresponse(data);});
		}
	});

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
	}
});