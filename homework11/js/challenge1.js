$(document).ready(function(event){

  $('#subscribe').change(function(event){
		if ($('input').is(':checked')) {
			$('#emailField').css('display','block');
		} else {
			$('#emailField').css('display','none');
		}
	});
});
