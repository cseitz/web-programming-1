# Web Programming 1
#### Subject Material & Review

## [Statc Files](./topic-01-static-file)
## [Bottle Essentials](./topic-02-bottle-intro)

## Additional info from other sources:

10 questions, same intensity as midterm
1. what are static files, things that parts of static files, contributary languages and services in static. Css, html
2. dynamic stuff, dynamic server. modify content before sending them out
3. templates, injecting content into webpage into setup before hosting : inject content inline, repeatedly content inline
4. how to use template, what aspect of template would you use to list students names and courses
5. forms, form tag, submit button sends the information back to server in post, also possible to use get which puts the data into a route. 
aware of fact that get request can be used in forms. form tag, input values, the submit part.
6. Cookies, small piece of data that is put on client in browser so browser can resubmit it next time to remidn the server what it was talking about. 
Causes a continuity between server and client since server is "stateless" and does not remember request
7. Sessions are continuity of actions stored on server. We get a cookie to match with session so we can load that session back. 
"do you locate shopping cart info on cookie, session or something else" we do something else. The cart is a property of customer so we store the cart in a 
database then connect the session to database then cookie to session.
8. Passwords and hashes. passwords arent storred

10. Understand what nginx, understand difference between static and redirected site
keep people off ports they dont need. CSS/HTML and a little about JS
Ask if somethings a HTML or JS problem etc
Talk about bootstrap library


static files - parts of static files
	html css javascript what do they do?
	dynamic-  bottle - modify content before sending out

templates - injecting content into webpage
	basic pattern 
	3 major patterns
		simply- inject in line
		conditionally -if else
		for loop-
	how would you use template functoinalty for student name and all courses
		name and campus and home address 
			inject name
			optionally inject student address on campus if not home 
			repitition - for loop
forms - form tag contains region of html that collects data in input statements
	when submit action is pressed it is sent back to server
		do it in post (puts it in body of request)
		get(puts it into route)-CAN BE USED LESS SECURE NOT AS LARGE THINGS
	form tag, input value, submit button

cookies - small piece of data put on client held by browser to resubmit to show what
		client was talking about, for continuity

server is stateless does not remember what client asks for
	once done its done - need coookies to procide ontinurty

sessions- info about continuty of series of interactions held on server (database or file)
	loading same info multiple request? use COOKIES

If you have a shoppping cart do you locate shopping cart info in cookie? in session? somewhere elese?
	- cookie remember session session remember idenity database uses identity to pull stuff up

profiles - profile vs session?
	-session remember current sequence of events on server or browser
	-profile long term piece of data about use or building etc etc

passwords - understand how storage and reterival
	store password as hash not as password
		submit password we hash it and compare to DB hash

understanding what engineX	
	static vs redirect dynamic site

keep people from ports to not use

CSS HTML JAVASCRIPT

is something html or css a problem why or because?

css selectors with [video explanation](https://seitz.sh/webprog/final-review?time=50.5)
```html
<style>

.whatever { color: red; }
#specific-div { background-color: blue; }
div { font-size: 50px; }
input[name="username"] { padding: 10px; }
div > span {}
div span {}
div.whatever {}

</style>

<div class="whatever" id="specific-div">
<input name="username">
<input name="password">
<div>
	<span>
		<p>
			<span>

            </span>
        </p>
    </span>
</div>

```

read javascript
	there is Ajax in javascript

understand CSS why bootstrap is important/ why is it sorta like CSS

*No questions on W3.css stuff* 

May be bootstrap stuff?