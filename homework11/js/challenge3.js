$(document).ready(function(event){
  $('#ch3form').submit(function(event){
    if ($('input:checked').length == 2) {
      return true;
    } else {
      alert("You must pick a class standing and a fruit!")
      return false;
    }
  });
});
