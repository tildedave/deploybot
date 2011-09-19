#!/usr/bin/python2.5

import tornado.ioloop
from tornado.web import StaticFileHandler
import tornado.template

from optparse import OptionParser

from index import IndexHandler
from plans import PlanHandler
from builds import BuildHandler
from environments import EnvironmentHandler
from deploy import DeployHandler
from tail import TailHandler

from environments import Environments
from api import BambooApi
from config import Config

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="config",
                      help="json config", metavar="JSON",
                      default="deploybot.json")
    parser.add_option("-p", "--port", dest="port",
                      help="port", metavar="JSON",
                      default="7070")
    
    (options, args) = parser.parse_args()

    config = Config(open(options.config).read())
    environments = Environments(config)
    api = BambooApi(config)

    loader = tornado.template.Loader("public/")
    
    application = tornado.web.Application([
        (r"/", IndexHandler, {"config": config, "loader" : loader}),
        (r"/plans/", PlanHandler, {"config": config, "api": api}),
        (r"/environments/(.*)", EnvironmentHandler, 
         {"config": config, 
          "environments": environments}),
        (r"/builds/(.*)", BuildHandler, 
         {"config": config, "api": api}),
        (r"/tail/", TailHandler, 
         {"config": config}),
        (r"/deploy/", DeployHandler, 
         {"config": config, 
          "environments" : environments,
          "loader": loader}),
        (r"/public/(.*)", StaticFileHandler, {"path": "public/"}),
        (r"/(favicon.ico)", StaticFileHandler, {"path": "public/"})
    ],debug=True)

    application.listen(int(options.port))
    application.debug = True
    tornado.ioloop.IOLoop.instance().start()
