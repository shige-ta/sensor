#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webapp2
import json
import logging
import time
import google.cloud.bigquery
from datetime import datetime
try:
    import pandas
except (ImportError, AttributeError):
    pandas = None
try:
    import pyarrow
except (ImportError, AttributeError):
    pyarrow = None
from google.appengine.ext import ndb


class People(ndb.Model):
    Humidity = ndb.StringProperty()
    temperature = ndb.StringProperty()
    pressure = ndb.StringProperty()
    date = ndb.StringProperty()
    img = ndb.BlobProperty(default=None)

class MainPage(webapp2.RequestHandler):


    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'

        people = People.query().fetch()
        p = people[-1]
        
        html = """
        <html>
            <head>
            <meta charset="utf-8">
            <title>
                test
            </title>
            <head>
            <body>
            湿度　%s％<br>
            温度　%s度<br>
            気圧　%shPa<br>
            最終取得時間　%s<br>
            </body>
        </html>
        """ % (p.Humidity.encode('utf-8'),p.temperature.encode('utf-8'), p.pressure.encode('utf-8'), p.date.encode('utf-8') )

        self.response.out.write(html)

    def post(self):

        data = json.loads(self.request.body)
        image_name = self.request.get('image_name')
        
        logging.debug(data)
        date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        d = People(Humidity=data["Humidity"],temperature=data["temperature"],pressure=data["pressure"], date=date,img=image_name)
        d.put()
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(data))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)