$(document).ready(function() {
	var number = parseInt($(document).find('#user').text(), 10);
	$(document).keydown(function(e){
		if (e.keyCode == 37) {
			window.location.replace('/self_human_move_left/'+number)
		}
		if (e.keyCode == 38) {
			window.location.replace('/self_human_move_up/'+number)
		}
		if (e.keyCode == 39) {
			window.location.replace('/self_human_move_right/'+number)
		}
		if (e.keyCode == 40) {
			window.location.replace('/self_human_move_down/'+number)
		}
	});
});