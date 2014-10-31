from django import forms
from django.utils.html import escape
from django.forms.util import flatatt
from django.utils.safestring import mark_safe


class GroupedSelect(forms.Select):
    """
        This is modified version of snippet https://djangosnippets.org/snippets/200/

        Please see https://djangosnippets.org/about/tos/ for license.

        Example:
        groceries = ((False, (('milk','milk'), (-1,'eggs'))), ('fruit', ((0,'apple'), (1,'orange'))), ('', (('yum','beer'), )),)
        grocery_list = GroupedChoiceField(choices=groceries)

        Renders:
        <select name="grocery_list" id="id_grocery_list">
            <option value="milk">milk</option>
            <option value="-1">eggs</option>
            <optgroup label="fruit">
                <option value="0">apple</option>
                <option value="1">orange</option>
            </optgroup>
            <option value="yum">beer</option>
        </select>
    """

    def render(self, name, value, attrs=None, choices=()):

        if value is None:
            value = ''

        final_attrs = self.build_attrs(attrs, name=name)
        output = ['<select%s>' % flatatt(final_attrs)]

        for group_label, group in self.choices:
            if group_label:
                output.append('<optgroup label="%s">' % escape(group_label))
            for option_value, option_label in group:
                selected_html = (option_value == value) and ' selected="selected"' or ''
                output.append(
                    '<option value="%s"%s>%s</option>' % (escape(option_value), selected_html, escape(option_label)))
            if group_label:
                output.append('</optgroup>')

        output.append('</select>')
        return mark_safe('\n'.join(output))
