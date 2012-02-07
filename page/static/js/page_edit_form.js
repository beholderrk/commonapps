var jQuery = django.jQuery || jQuery || $;
jQuery(function ($) {
    $(".open_window").fancybox({
//        maxWidth	: 800,
//        maxHeight	: 600,
        fitToView	: false,
//        width		: '70%',
//        height		: '70%',
        autoSize	: false,
        closeClick	: false,
        openEffect	: 'none',
        closeEffect	: 'none'
    });
});