var $ = django.jQuery || jQuery;

function addEditor(){
    $('.ckeditor_inline').each(function(){
        if($(this).parents('div.empty-form').length == 0 && $(this).parents('fieldset.collapsed').length == 0){
            try{
                CKEDITOR.replace($(this).attr('id'));
            }
            catch(err){}
        }
    });
}

function addNewInline(){
    try{
        createTabs(true);
    }
    catch(err){}
    addEditor();
}

$(document).ready(function() {
    addEditor();
});