$(document).ready(function(){
    $('.collapsible').collapsible();
    $("#search").focus(function() {
    $(".search-box").addClass("border-searching");
    $(".search-icon").addClass("si-rotate");
    $('.sidenav').sidenav();
    $('.datepicker').datepicker();
});

// $(document).ready(function(){
// $('.sidenav').sidenav();
// });

// $(document).ready(function(){
// $("#search").focus(function() {
//     $(".search-box").addClass("border-searching");
//     $(".search-icon").addClass("si-rotate");
// });

$("#search").blur(function() {
    $(".search-box").removeClass("border-searching");
    $(".search-icon").removeClass("si-rotate");
});

$("#search").keyup(function() {
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

// $(document).ready(function(){
// $('.datepicker').datepicker();
// });