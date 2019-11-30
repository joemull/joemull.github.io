useBilling.onchange = function() {
	let home = document.querySelector("#home");
	let billing = document.querySelector("#billing");

	if (this.checked){
		home.value = billing.value;
		home.disabled = true;}
	else {
		home.value = "";
		home.disabled = false;}
	
	}