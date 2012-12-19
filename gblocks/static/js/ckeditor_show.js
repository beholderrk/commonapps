var $ = django.jQuery || jQuery;

$(function(){
	var editor;
	$('textarea').each(function(i){
		$(this).before('<a href="" class="enable_ck" style="display: block; clear: both;">on ckeditor</a>');
	});
	$('.enable_ck').live('click', function(e){
		e.preventDefault();
		editor = CKEDITOR.replace($(this).next()[0]);
		$(this).attr('class', 'remove_ck').text('off ckeditor');
	});
	$('.remove_ck').live('click', function(e){
		e.preventDefault();
		editor.destroy();
		$(this).attr('class', 'enable_ck').text('on ckeditor');
	});
});