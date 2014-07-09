$(document).ready(function() {
	 $('super-slow').click(function() {
	 	$.get('/set_speed', {speed: superslow}, function() {});
	 })
	 $('slow').click(function() {
	 	$.get('/set_speed', {speed: slow}, function() {});
	 })
	 $('mid').click(function() {
	 	$.get('/set_speed', {speed: mid}, function() {});
	 })
	 $('fast').click(function() {
	 	$.get('/set_speed', {speed: fast}, function() {});
	 })
	 $('super-fast').click(function() {
	 	$.get('/set_speed', {speed: superfast}, function() {});
	 })
});