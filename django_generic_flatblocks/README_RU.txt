Приложение django_generic_flatblocks с расширенным тегом gblock.

В расширенном теге gblock можно указывать инлайны которые должны отображаться при 
редактировании CustomBlock в админке.

{% gblock 'video_block' for 'gblocks.CustomBlock' visible_inlines  'AttachedSimpleTextInline,AttachedRichTextInline,AttachedLinkInline' %}

Если параметр visible_inlines опущен, отображаются все инлайны. 