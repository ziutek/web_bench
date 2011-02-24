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
    if len(argv) > 2:
        sname = argv[1]
        port = int(argv[2])
        if sname == "cherrypy":
            from web.wsgiserver import CherryPyWSGIServer as WSGIServer
            server = WSGIServer(("0.0.0.0", port), wsgifunc,
                                request_queue_size=40)
            try:
                server.start()
            except KeyboardInterrupt:
                server.stop()
        elif sname == "gevent":
            from gevent.wsgi import WSGIServer
            server = WSGIServer(("0.0.0.0", port), wsgifunc, log=None)
            server.serve_forever()
        else:
            print "Unknown server"
    else:
        from flup.server.fcgi import WSGIServer
        server = WSGIServer(wsgifunc, bindAddress=None,
                            multiplexed=False, multithreaded=False)
        server.run()
        #web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
        #app.run()
