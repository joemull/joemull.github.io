$(document).ready(function(event){
  $('#ch4form').submit(function(event){
    $('#nameerrormsg').css('display','none');
    $('#addrerrormsg').css('display','none');
    if ($('#fullname').val() == '') {
      $('#nameerrormsg').css('display','block');
      $('#fullname').focus();
      return false;
    } else if ($('#streetaddr').val() == '') {
      $('#addrerrormsg').css('display','block');
      $('#streetaddr').focus();
      return false;
    }
    return true;
  });
});
