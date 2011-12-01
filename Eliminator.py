import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
import httpagentparser

class Check(webapp.RequestHandler):
    def get(self):
        if self.request.path.find("check") != -1:
            user_agent = self.request.headers['User-Agent']
            browser = httpagentparser.detect(user_agent)['browser']
            url = self.request.get('url', default_value='/')
            if url!='/' and (url.find('://') not in range(2,8)):
                url = 'http://' + url
            if browser['name'].find('Internet Explorer')==-1 or browser['version'].find('6.0')!=0:
                self.redirect(url)
            else:
                path = os.path.join(os.path.dirname(__file__), 'templates/eliminator_en.html')
                self.response.out.write(template.render(path, {'url': url}))
        else:
            self.response.set_status(404)

    def post(self):
        if self.request.path.find("preview") != -1:
            url = self.request.get('url', default_value='/')
            if url!='/' and (url.find('://') not in range(2,8)):
                url = 'http://' + url
            path = os.path.join(os.path.dirname(__file__), 'templates/eliminator_en.html')
            self.response.out.write(template.render(path, {'url': url, 'is_preview': True}))
        else:
            self.response.set_status(404)
