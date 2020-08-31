$(document).ready(function(){
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.sidenav').sidenav();
    $('.datepicker').datepicker();
    $('.resource_updated')
    $("#searchbox").focus(function() {
    $(".search-box").addClass("border-searching");
    $(".search-icon").addClass("si-rotate");
});
});

$("#searchbox").blur(function() {
    $(".search-box").removeClass("border-searching");
    $(".search-icon").removeClass("si-rotate");
});

$("#searchbox").keyup(function() {
    if($(this).val().length > 0) {
        $(".go-icon").addClass("go-in");
    }
    else {
        $(".go-icon").removeClass("go-in");
    }
});

$(".go-icon").click(function(){
    $(".search-form").submit();
});

$( "#addresource" ).click(function() {
  alert( "Handler for .click() called." );
});