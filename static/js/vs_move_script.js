$(document).ready(function() {
	var number = parseInt($(document).find('#user').text(), 10);
	var time = parseInt($(document).find('#time').text(), 10);
	var maxTime = parseInt($(document).find('#max_time').text(), 10);
	var gameWidth = $("#human-game-container").width();
	var margin = parseInt($('#games-container').css("marginLeft"));
	var total = $('body').width();
	var optionsWidth = total - 2*gameWidth - 4*margin;
	$('.options-vs').width(optionsWidth);
	console.log(margin+gameWidth);
	$('#options-container-vs').css('left', margin+gameWidth);
	$('#options-container-vs').width(optionsWidth)
	console.log(margin);
	console.log(optionsWidth);
	$(document).keydown(function(e){
		if (e.keyCode == 37) {
			window.location.replace('/vs_human_move_left/'+number+'/'+Math.round(window.performance.now()+time))
		}
		if (e.keyCode == 38) {
			window.location.replace('/vs_human_move_up/'+number+'/'+Math.round(window.performance.now()+time))
		}
		if (e.keyCode == 39) {
			window.location.replace('/vs_human_move_right/'+number+'/'+Math.round(window.performance.now()+time))
		}
		if (e.keyCode == 40) {
			window.location.replace('/vs_human_move_down/'+number+'/'+Math.round(window.performance.now()+time))
		}
	});
	setTimeout(function(){window.location.replace('/vs_ai_move/'+number+'/0')}, maxTime-time);
});