#!/usr/bin/env python
from sys import argv
import web

class ServeHTTP(object):
    def GET(self, txt, num):
        try:
            n = int(num)
        except ValueError:
            return
        for i in xrange(n):
            yield "%d: %s\n" % (i, txt)


web.config.debug = False
urls = ("^/([^/]+)/([^/]+)$", "ServeHTTP")
app = web.application(urls, globals())
wsgifunc = app.wsgifunc()

if __name__ == "__main__":
    if len(argv) > 1 :
        from web.wsgiserver import CherryPyWSGIServer
        server = CherryPyWSGIServer(("0.0.0.0", int(argv[1])),
                                    wsgifunc, request_queue_size=40)
        try:
            server.start()
        except KeyboardInterrupt:
            server.stop()
    else:
        from flup.server.fcgi import WSGIServer
        server = WSGIServer(wsgifunc, bindAddress=None,
                            multiplexed=False, multithreaded=False)
        server.run()
        #web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
        #app.run()
