import tornado.ioloop
import tornado.web
import tornado.log

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Hello, world")
    self.set_header("Content-Type", 'text/plain')
def make_app():
  return tornado.web.Application([
    (r"/", MainHandler),
  ], autoload=True)
if __name__ == "__main__":
  tornado.log.enable_pretty_logging()
  
  app = make_app()
  app.listen(8888)
  tornado.ioloop.IOLoop.current().start()