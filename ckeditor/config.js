/*
Copyright (c) 2003-2010, CKSource - Frederico Knabben. All rights reserved.
For licensing, see LICENSE.html or http://ckeditor.com/license
*/

CKEDITOR.editorConfig = function( config )
{
	// Define changes to default configuration here. For example:
	config.language = 'ru';
//	config.uiColor = '#AADC6E';
    config.filebrowserBrowseUrl = '/admin/filebrowser/browse/?pop=3';
    config.toolbar = 'kobe';
    config.toolbar_Basic =
    [
        [      'Undo', 'Redo',
          '-', 'Bold', 'Italic', 'Underline','Subscript','Superscript',
          '-', 'Link', 'Unlink', 'Anchor',
          '-', 'Format','RemoveFormat',
          '-', 'Maximize'
        ],
        [      'HorizontalRule',
          '-', 'Image','Table',
          '-', 'BulletedList', 'NumberedList','Outdent','Indent',
          '-', 'Cut','Copy','Paste','PasteText','PasteFromWord',
          '-', 'SpecialChar',
          '-', 'Source',
          '-', 'About'
        ]
    ];

    config.toolbar_kobe =
    [
        [ 'Source','-','Preview','-','Templates' ],
        [ 'Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo' ],
        [ 'Find','Replace','-','SelectAll','-', 'Scayt' ],
        [ 'Bold','Italic','Underline','Strike','Subscript','Superscript','-','RemoveFormat' ],
        [ 'Maximize', 'ShowBlocks'],
        [ 'NumberedList','BulletedList','-','Outdent','Indent','-','Blockquote','CreateDiv','-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock','-','BidiLtr','BidiRtl' ],
        [ 'Link','Unlink','Anchor' ],
        [ 'Image','Table','HorizontalRule','SpecialChar'],
        [ 'Format','FontSize' ],
        [ 'TextColor','BGColor' ]
    ];

    config.width = 750;
//    config.skin = 'v2';
    config.toolbarCanCollapse = true;
};
