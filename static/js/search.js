// BOXOFFICE 1st
$(document).ready(function(){
    $('.carousel').carousel({padding:250, dist:0});
    $('.rate_wrap').carousel({dist:-100});
    $('.review_wrap').carousel({dist:-100});

    $(".card_wrap_1").hover(function(){
        $(".card_info_1").addClass("card_info_hover");
        $(".card_image_1").addClass("card_image_hover");
    });

    $(".card_wrap_1").mouseleave(function(){
        $('.card_info_1').removeClass("card_info_hover");
        $(".card_image_1").removeClass("card_image_hover");
    });

    // BOXOFFICE 2nd
    $(".card_wrap_2").hover(function(){
        $(".card_info_2").addClass("card_info_hover");
        $(".card_image_2").addClass("card_image_hover");
    });

    $(".card_wrap_2").mouseleave(function(){
        $('.card_info_2').removeClass("card_info_hover");
        $(".card_image_2").removeClass("card_image_hover");
    });

    // BOXOFFICE 3rd
    $(".card_wrap_3").hover(function(){
        $(".card_info_3").addClass("card_info_hover");
        $(".card_image_3").addClass("card_image_hover");
    });

    $(".card_wrap_3").mouseleave(function(){
        $(".card_info_3").removeClass("card_info_hover");
        $(".card_info_3").removeClass("card_image_hover");
    });

    // BOXOFFICE 4th
    $(".card_wrap_4").hover(function(){
        $(".card_info_4").addClass("card_info_hover");
        $(".card_image_4").addClass("card_image_hover");
    });

    $(".card_wrap_4").mouseleave(function(){
        $('.card_info_4').removeClass("card_info_hover");
        $(".card_image_4").removeClass("card_image_hover");
    });

    // BOXOFFICE 5th
    $(".card_wrap_5").hover(function(){
        $(".card_info_5").addClass("card_info_hover");
        $(".card_image_5").addClass("card_image_hover");
    });

    $(".card_wrap_5").mouseleave(function(){
        $('.card_info_5').removeClass("card_info_hover");
        $(".card_image_5").removeClass("card_image_hover");
    });

    // Bottom 1st
    $(".card_wrap_5").mouseleave(function(){
        $('.card_info_5').removeClass("card_info_hover");
        $(".card_image_5").removeClass("card_image_hover");
    });
});

