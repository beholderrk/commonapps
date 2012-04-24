//(function(b){b.fn.formset=function(g){var a=b.extend({},b.fn.formset.defaults,g),k=function(c,f,d){var e=new RegExp("("+f+"-(\\d+|__prefix__))");f=f+"-"+d;b(c).attr("for")&&b(c).attr("for",b(c).attr("for").replace(e,f));if(c.id)c.id=c.id.replace(e,f);if(c.name)c.name=c.name.replace(e,f)};g=b("#id_"+a.prefix+"-TOTAL_FORMS").attr("autocomplete","off");var l=parseInt(g.val()),h=b("#id_"+a.prefix+"-MAX_NUM_FORMS").attr("autocomplete","off");g=h.val()==""||h.val()-g.val()>0;b(this).each(function(){b(this).not("."+
//a.emptyCssClass).addClass(a.formCssClass)});if(b(this).length&&g){var j;if(b(this).attr("tagName")=="TR"){g=this.eq(0).children().length;b(this).parent().append('<tr class="'+a.addCssClass+'"><td colspan="'+g+'"><a href="javascript:void(0)">'+a.addText+"</a></tr>");j=b(this).parent().find("tr:last a")}else{b(this).filter(":last").after('<div class="'+a.addCssClass+'"><a href="javascript:void(0)">'+a.addText+"</a></div>");j=b(this).filter(":last").next().find("a")}j.click(function(){var c=b("#id_"+
//a.prefix+"-TOTAL_FORMS"),f=b("#"+a.prefix+"-empty"),d=f.clone(true);d.removeClass(a.emptyCssClass).addClass(a.formCssClass).attr("id",a.prefix+"-"+l);if(d.is("tr"))d.children(":last").append('<div><a class="'+a.deleteCssClass+'" href="javascript:void(0)">'+a.deleteText+"</a></div>");else d.is("ul")||d.is("ol")?d.append('<li><a class="'+a.deleteCssClass+'" href="javascript:void(0)">'+a.deleteText+"</a></li>"):d.children(":first").append('<span><a class="'+a.deleteCssClass+'" href="javascript:void(0)">'+
//a.deleteText+"</a></span>");d.find("*").each(function(){k(this,a.prefix,c.val())});d.insertBefore(b(f));b(c).val(parseInt(c.val())+1);l+=1;h.val()!=""&&h.val()-c.val()<=0&&j.parent().hide();d.find("a."+a.deleteCssClass).click(function(){var e=b(this).parents("."+a.formCssClass);e.remove();l-=1;a.removed&&a.removed(e);e=b("."+a.formCssClass);b("#id_"+a.prefix+"-TOTAL_FORMS").val(e.length);if(h.val()==""||h.val()-e.length>0)j.parent().show();for(var i=0,m=e.length;i<m;i++){k(b(e).get(i),a.prefix,i);
//b(e.get(i)).find("*").each(function(){k(this,a.prefix,i)})}return false});a.added&&a.added(d);return false})}return this};b.fn.formset.defaults={prefix:"form",addText:"add another",deleteText:"remove",addCssClass:"add-row",deleteCssClass:"delete-row",emptyCssClass:"empty-row",formCssClass:"dynamic-form",added:null,removed:null}})(django.jQuery);


/**
 * Django admin inlines
 *
 * Based on jQuery Formset 1.1
 * @author Stanislaus Madueke (stan DOT madueke AT gmail DOT com)
 * @requires jQuery 1.2.6 or later
 *
 * Copyright (c) 2009, Stanislaus Madueke
 * All rights reserved.
 *
 * Spiced up with Code from Zain Memon's GSoC project 2009
 * and modified for Django by Jannis Leidel
 *
 * Licensed under the New BSD License
 * See: http://www.opensource.org/licenses/bsd-license.php
 */
(function($) {
    $.fn.formset = function(opts) {
        var options = $.extend({}, $.fn.formset.defaults, opts);
        var updateElementIndex = function(el, prefix, ndx) {
            var id_regex = new RegExp("(" + prefix + "-(\\d+|__prefix__))");
            var replacement = prefix + "-" + ndx;
            if ($(el).attr("for")) {
                $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
            }
            if (el.id) {
                el.id = el.id.replace(id_regex, replacement);
            }
            if (el.name) {
                el.name = el.name.replace(id_regex, replacement);
            }
        };
        var totalForms = $("#id_" + options.prefix + "-TOTAL_FORMS").attr("autocomplete", "off");
        var nextIndex = parseInt(totalForms.val());
        var maxForms = $("#id_" + options.prefix + "-MAX_NUM_FORMS").attr("autocomplete", "off");
        // only show the add button if we are allowed to add more items,
        // note that max_num = None translates to a blank string.
        var showAddButton = maxForms.val() == '' || (maxForms.val()-totalForms.val()) > 0;
        $(this).each(function(i) {
            $(this).not("." + options.emptyCssClass).addClass(options.formCssClass);
        });
        if ($(this).length && showAddButton) {
            var addButton;
            if ($(this).attr("tagName") == "TR") {
                // If forms are laid out as table rows, insert the
                // "add" button in a new table row:
                var numCols = this.eq(0).children().length;
                $(this).parent().append('<tr class="' + options.addCssClass + '"><td colspan="' + numCols + '"><a href="javascript:void(0)">' + options.addText + "</a></tr>");
                addButton = $(this).parent().find("tr:last a");
            } else {
                // Otherwise, insert it immediately after the last form:
                $(this).filter(":last").after('<div class="' + options.addCssClass + '"><a href="javascript:void(0)">' + options.addText + "</a></div>");
                addButton = $(this).filter(":last").next().find("a");
            }
            addButton.click(function() {
                var totalForms = $("#id_" + options.prefix + "-TOTAL_FORMS");
                var template = $("#" + options.prefix + "-empty");
                var row = template.clone(true);
                row.removeClass(options.emptyCssClass)
                    .addClass(options.formCssClass)
                    .attr("id", options.prefix + "-" + nextIndex);
                if (row.is("tr")) {
                    // If the forms are laid out in table rows, insert
                    // the remove button into the last table cell:
                    row.children(":last").append('<div><a class="' + options.deleteCssClass +'" href="javascript:void(0)">' + options.deleteText + "</a></div>");
                } else if (row.is("ul") || row.is("ol")) {
                    // If they're laid out as an ordered/unordered list,
                    // insert an <li> after the last list item:
                    row.append('<li><a class="' + options.deleteCssClass +'" href="javascript:void(0)">' + options.deleteText + "</a></li>");
                } else {
                    // Otherwise, just insert the remove button as the
                    // last child element of the form's container:
                    row.children(":first").append('<span><a class="' + options.deleteCssClass + '" href="javascript:void(0)">' + options.deleteText + "</a></span>");
                }
                row.find("*").each(function() {
                    updateElementIndex(this, options.prefix, totalForms.val());
                });
                // Insert the new form when it has been fully edited
                row.insertBefore($(template));
                // Update number of total forms
                $(totalForms).val(parseInt(totalForms.val()) + 1);
                nextIndex += 1;
                // Hide add button in case we've hit the max, except we want to add infinitely
                if ((maxForms.val() != '') && (maxForms.val()-totalForms.val()) <= 0) {
                    addButton.parent().hide();
                }
                // The delete button of each row triggers a bunch of other things
                row.find("a." + options.deleteCssClass).click(function() {
                    // Remove the parent form containing this button:
                    var row = $(this).parents("." + options.formCssClass);
                    row.remove();
                    nextIndex -= 1;
                    // If a post-delete callback was provided, call it with the deleted form:
                    if (options.removed) {
                        options.removed(row);
                    }
                    // Update the TOTAL_FORMS form count.
                    var forms = $("." + options.formCssClass);
                    $("#id_" + options.prefix + "-TOTAL_FORMS").val(forms.length);
                    // Show add button again once we drop below max
                    if ((maxForms.val() == '') || (maxForms.val()-forms.length) > 0) {
                        addButton.parent().show();
                    }
                    // Also, update names and ids for all remaining form controls
                    // so they remain in sequence:
                    for (var i=0, formCount=forms.length; i<formCount; i++)
                    {
                        updateElementIndex($(forms).get(i), options.prefix, i);
                        $(forms.get(i)).find("*").each(function() {
                            updateElementIndex(this, options.prefix, i);
                        });
                    }
                    return false;
                });
                // If a post-add callback was supplied, call it with the added form:
                if (options.added) {
                    options.added(row);
                }
                //createTabs(true);
                //var fs = $('div.last_related:not(.empty_form)').find('fieldset');
                //if(!fs.hasClass('collapsed')){
					//addEditor();
                //}
                //alert('4');
                addNewInline()
                return false;
            });
        }
        return this;
    }
    /* Setup plugin defaults */
    $.fn.formset.defaults = {
        prefix: "form",					// The form prefix for your django formset
        addText: "add another",			// Text for the add link
        deleteText: "remove",			// Text for the delete link
        addCssClass: "add-row",			// CSS class applied to the add link
        deleteCssClass: "delete-row",	// CSS class applied to the delete link
        emptyCssClass: "empty-row",		// CSS class applied to the empty row
        formCssClass: "dynamic-form",	// CSS class applied to each form in a formset
        added: null,					// Function called each time a new form is added
        removed: null					// Function called each time a form is deleted
    }
})(django.jQuery);
