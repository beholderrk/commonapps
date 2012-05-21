/**
 * User: beholder
 * Date: 3/6/12
 * Time: 10:28 AM
 */
$(function(){
    $('[rel=inlineedit]').each(function(){
        var link = "<a class='inlineEditLink %s' target='_blank' href='%s'></a>";
        var elem = $(this);
        var adminurl = $(this).data('adminurl');
        var css_class = $(this).data('class');
        elem.append(sprintf(link, css_class, adminurl));
        $(this).hover(
            function(){
                $('.inlineEditLink', this).stop().fadeIn().css({ display: 'inline-block'});
            },
            function(){
                $('.inlineEditLink', this).stop().fadeOut();
            }
        );
    });
});