##Required Python Package: 
lpthw.web or web.py

sudo -H pip install lpthw.web

## Make a Simple "Hello World" Project
Now you're going to make an initial very simple "Hello World" web
application and project directory using lpthw.web. First, make your project directory:
'''
$ cd projects
$ mkdir gothonweb
$ cd gothonweb
$ mkdir bin gothonweb tests docs templates
$ touch gothonweb/__init__.py
$ touch tests/__init__.py
'''
You'll be taking the game from Exercise 43 and making it into a web application,
so that's why you're calling it gothonweb
Before you do that, we need to create the most basic lpthw.web application
possible. You need to write following in bin/app.py for actual web app to work
'''python
import web

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
'''
### Then run the application like this:
'''
$ python bin/app.py
http://0.0.0.0:8080/
However, if you did this:

$ cd bin/   # WRONG! WRONG! WRONG!
$ python app.py  # WRONG! WRONG! WRONG!
'''
Then you are doing it wrong. In all Python projects you do not cd into a
lower directory to run things. You stay at the top and run everything from
there so that all of the system can access all the modules and files.
# Finally, use your web browser and go to http://localhost:8080/ and 
you should see two things. First, in your browser you'll see 
Hello, world!. Second, you'll see your Terminal with new output like this:
'''
$ python bin/app.py
http://0.0.0.0:8080/
127.0.0.1:59542 - - [13/Jun/2011 11:44:43] "HTTP/1.1 GET /" - 200 OK
127.0.0.1:59542 - - [13/Jun/2011 11:44:43] "HTTP/1.1 GET /favicon.ico" - 404 Not Found
'''
Those are log messages that lpthw.web prints out so you can see that the
server is working, and what the browser is doing behind the scenes. The log
messages help you debug and figure out when you have problems. For example,
it's saying that your browser tried to get /favicon.ico but that file didn't 
exist so it returned 404 Not Found status code.



## Create Basic Templates

 This is a web application, and as such it needs a proper HTML response.
 To do that you will create a simple template that says "Hello World" in a
 big green font.
 
First step to create a templates/index.html file for the homepage of web app.

This HTML file, however, is a template, which means that lpthw.web
will fill in "holes" in the text depending on variables you pass in to the
template. Every place you see $greeting will be a variable you'll pass to 
the template that alters its contents.

To make your bin/app.py do this, you need to add some code to tell lpthw.web
where to load the template and to render it. Take that file and change it like this:
'''python
import web

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
'''
### In your bin/app.py you've added a new variable, render, which is a
  web.template.render object.
  
### This render object knows how to load .html files out of the 
  templates/ directory because you passed that to it as a parameter.

### Later in your code, when the browser hits the index.GET like before, 
  instead of just returning the string greeting, you call render.index 
  and pass the greeting to it as a variable.
  
### This render.index method is kind of a magic function where the render 
  object sees that you're asking for index, goes into the templates/ directory, 
  looks for a page named index.html, and then "renders" it, or converts it.

### In the templates/index.html file you see the beginning definition that says
  this template takes a greeting parameter, just like a function. Also, just
  like Python this template is indentation sensitive, so make sure you get them right.

### Finally, you have the HTML in templates/index.html that looks at the greeting
  variable and, if it's there, prints one message using the $greeting, or a
  default message.
  
  
## Why do we assign greeting=greeting when we call the template?
    
	You are not assigning to greeting. You are setting a named parameter to 
	give to the template. It's sort of an assignment, but it only affects the
	call to the template function.
