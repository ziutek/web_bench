#!/usr/bin/env python
import sys
import web
from web.wsgiserver import CherryPyWSGIServer

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
server = CherryPyWSGIServer(("0.0.0.0", int(sys.argv[1])), app.wsgifunc(),
                            request_queue_size=20)

if __name__ == "__main__":
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
