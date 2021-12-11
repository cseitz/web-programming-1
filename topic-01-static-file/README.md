Static `.html` files can be served via a variety of ways.

[Introduction to HTML](https://www.w3schools.com/html/html_intro.asp)

HTML utilizes XML tags
```html
<openingTag>
    text content or even more tags
</closingTag>
```

Some tags do not require a closing tag. Here are a few that you'll actually use. Full list can be found [here](https://www.thoughtco.com/html-singleton-tags-3468620).
- br
- hr
- img
- input
- link

HTML files start with `<!DOCTYPE html>` *(no longer required, yet still highly recommended)* and are followed by a `<html>` opening tag.

They are followed by an optional `<head>` element that contains many resources that do not get rendered. Here is where you would import stylesheets or set the document's title.

After closing the head tag with `</head>`, then the website body is identified with `<body>`. In here is where all your content will go.