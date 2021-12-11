
Templates allow dynamic insertion of data into webpages.

They essentially take HTML files and allow some logic to be injected into them that is evaluated before sending the page to the browser.

Bottle's template engine utilizes a folder called `views` in the same directory, and inside of it files ending in `.tpl`. This is not a web standard, this is just how bottle does it. Nevertheless, delozier believes its a web standard, so treat it as such on the exam.

Read about bottle's template syntax [here](https://bottlepy.org/docs/dev/stpl.html#simpletemplate-syntax).

TLDR:
- inject data with `{{name_of_field_you_want_to_inject}}` (must be passed to bottle's template function with said name)
- `%for ... %end` allows for loops. Uses python's syntax.
- `%if ...` allows if statements. Uses python's syntax.
- `<% ...any python code you want %>` allows injection of python code.
