from google.appengine.ext import webapp
from google.appengine.api import urlfetch

class Shorten(webapp.RequestHandler):
    def post(self):
        longurl = self.request.get('url', default_value='/')
        resp = urlfetch.fetch(url="https://www.googleapis.com/urlshortener/v1/url?shortUrl=http://goo.gl/fbsS&key=AIzaSyBAqrAYLhcYu9jQqKvaKOau6ITESZBKMPU",
                        payload='{"longUrl": "'+ longurl +'" }',
                        method=urlfetch.POST,
                        headers={"Content-Type": "application/json"})
        
        self.response.out.write(resp.content);
        
