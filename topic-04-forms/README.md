HTML Forms are the standard way to have groups of input fields
that allow user input.

For example, logging into a website can utilize a form that groups the
username and password inputs and allows those to be submitted to a server
by triggering the form submission. No JavaScript requires.

Forms are still widely in use today, but modern web design avoids forms
and utilizes JavaScript instead to get real-time validation of inputted
data.

A `<form>` has a `action` and `method` attribute that specifies the URL to send the data to, using the specified HTTP method. In most cases, method will be `post` or sometimes `put`, but **never** `get` since `get` does not allow for a request body.

Forms can be triggered by having an `<input type="submit" value="submit form">` within the form, which when clicked will trigger form submission.

