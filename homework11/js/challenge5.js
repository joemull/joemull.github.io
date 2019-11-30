$(document).ready(function(event){
	function disp(chosen) {
		$('#image').css('backgroundImage',
			"url('"+ $(chosen).attr('src') +"')");
		$('#image').attr('alt',$(chosen).attr('alt'));
		$('#image').html($(chosen).attr('alt'));
	}

	$('img').mouseover(function(event){
		disp(this);
	});

	$('img').focus(function(event){
		disp(this);
	});

	function undisp() {
		$('#image').css('backgroundImage',"url('')");
		$('#image').attr('alt','');
		$('#image').html('<p>Hover over an image below.</p>');
	}

	$('img').mouseleave(function(event){
		undisp();
	});

	$('img').blur(function(event){
		undisp();
	});

});
	
