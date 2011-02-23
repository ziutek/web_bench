#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.web

class ServeHTTP(tornado.web.RequestHandler):
    def get(self, txt, num):
        for i in xrange(int(num)):
            self.write("%d: %s\n" % (i, txt))


urls = [
    ("^/([^/]+)/([0-9]+)$", ServeHTTP)
]
app = tornado.web.Application(urls)

if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
