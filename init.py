from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from HomePage import *
from Eliminator import *
from Shorten import *

application = webapp.WSGIApplication(
        [('/', HomePage),('/check',Check),('/preview',Check),('/shorten',Shorten)],
        debug=False)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
