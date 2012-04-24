var $ = django.jQuery || jQuery;


//function addEditor(){
//    $('.ckeditor_inline').each(function(){
//        if($(this).parents('div.empty-form').length == 0 && $(this).parents('fieldset.collapsed').length == 0){
//            try{
//                CKEDITOR.replace($(this).attr('id'));
//            }
//            catch(err){}
//        }
//    });
//}
//
//function addNewInline(){
//    try{
//        createTabs(true);
//    }
//    catch(err){}
//    addEditor();
//}

//(function($) {
    $(document).ready(function() {
        // Only for stacked inlines
        $('div.inline-group div.inline-related:not(.tabular)').each(function() {
            var fs = $(this).find('fieldset')
            var h3 = $(this).find('h3:first')

            // Don't collapse if fieldset contains errors
            if (fs.find('div').hasClass('errors'))
                fs.addClass('stacked_collapse');
            else
                fs.addClass('stacked_collapse collapsed');

            // Add toggle link
            h3.prepend('<a class="stacked_collapse-toggle" href="#">(' + gettext('Show') + ')</a> ');

            h3.bind("click", function(){
                fs = $(this).next('fieldset');
                var collapsed = fs.hasClass('collapsed')
                var dv = $(this).parents('div.inline-group');

                dv.find('fieldset').addClass('collapsed');
                dv.find('a.stacked_collapse-toggle').html('(' + gettext('Show') + ')');

                var h3_a = $(this).find('a.stacked_collapse-toggle');

                if (!collapsed)
                {
                    fs.addClass('collapsed');
                    h3_a.html('(' + gettext('Show') + ')');
                }
                else
                {
                    fs.removeClass('collapsed');
                    h3_a.html('(' + gettext('Hide') + ')');
                }
            }).css('cursor', 'pointer');
        });

        $('div.inline-group').each(function() {
            var h2 = $(this).find('h2');
            var fss = $(this).find('fieldset');
            var fss_a = $(this).find('a.stacked_collapse-toggle');

//            h2.append(' <a class="stacked_all_collapse-toggle" href="#">(' + gettext('Show') + ')&darr;</a> ').addClass('collapsed');
            h2.append(' <a class="stacked_all_collapse-toggle" href="#" title="Expand/Collapse">&nbsp;▲ ▼</a> ').addClass('collapsed');
            fss.addClass('collapsed');
            var h2_a = h2.find('a.stacked_all_collapse-toggle');

            h2.bind("click", function(){
                fss = $(this).parents('div.inline-group').find('fieldset');
                h2.toggleClass('collapsed');
                if(h2.hasClass('collapsed')){
                    fss.addClass('collapsed');
                    fss_a.html('(' + gettext('Show') + ')');
                }
                else{
                    fss.removeClass('collapsed');
                    fss_a.html('(' + gettext('Hide') + ')');
                }
            }).css('cursor', 'pointer');
        });



//        $('.ckeditor_test').live('click', function(){
//            CKEDITOR.replace($(this).attr('id'));
//        });

        $('div.inline-group').live('click', function(){
            try{
                createTabs(true);
            }
            catch(err){}
            addEditor();
        });
    });
//})(django.jQuery);