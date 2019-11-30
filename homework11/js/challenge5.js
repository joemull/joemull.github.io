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

// $(document).ready(function(){
// 	$('img').mouseover(function(){
// 		$('#image').css('backgroundImage',
// 			"url('"+ $(this).attr('src') +"')");
// 		$('#image').attr('alt',$(this).attr('alt'));
// 		$('#image p').HTML($(this).attr('alt'));
// 	});
// 	$('img').mouseleave(function(){
// 		$('#image').css('backgroundImage',"url('')");
// 		$('#image').attr('alt','');
// 		$('#image p').HTML('');
// 	});
// });

// console.log("here")
// var imgs = document.querySelectorAll("img");
// var msg = "Hover over an image below."
// for (let i = 0; i < imgs.length;i++){
// 	imgs[i].onmouseover = function() {
// 	 	document.querySelector('#image').style.backgroundImage="url('"+imgs[i].src+"')";
// 	 	document.querySelector('#image').innerHTML= imgs[i].alt;
// 	 }
//
// 	 imgs[i].onfocus = function() {
// 	 	document.querySelector('#image').style.backgroundImage="url('"+imgs[i].src+"')";
// 	 	document.querySelector('#image').innerHTML= imgs[i].alt;
// 	 }
//
// 	 imgs[i].onmouseleave = function() {
// 	 	document.querySelector('#image').style.backgroundImage="url('')";
// 	 	document.querySelector('#image').innerHTML= msg;
// 	 }
//
// 	 imgs[i].onblur = function() {
// 	 	document.querySelector('#image').style.backgroundImage="url('')";
// 	 	document.querySelector('#image').innerHTML= msg;
// 	 }
// }
