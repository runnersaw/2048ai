$(document).ready(function() {
	var number = parseInt($(document).find('#user').text(), 10);
	var maxTime = parseInt($(document).find('#max_time').text(), 10);
	setTimeout(function(){window.location.replace('/ai_move/'+number)}, maxTime);
});