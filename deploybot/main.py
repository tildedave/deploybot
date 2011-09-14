#!/usr/bin/python2.5

import tornado.ioloop
from tornado.web import StaticFileHandler
import tornado.template

from optparse import OptionParser
from ConfigParser import RawConfigParser

from index import IndexHandler
from plans import PlanHandler
from builds import BuildHandler
from deploy import DeployHandler
from api import BambooApi
from config import Config

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="config",
                      help="config file", metavar="CONFIG",
                      default="deploybot.conf")
    
    (options, args) = parser.parse_args()

    raw_parser = RawConfigParser()
    raw_parser.readfp(open(options.config))
    config = Config(raw_parser)
    api = BambooApi(config)

    loader = tornado.template.Loader("static/")
    
    application = tornado.web.Application([
        (r"/", IndexHandler, {"config": config, "loader" : loader}),
        (r"/plans/", PlanHandler, {"config": config, "api": api}),
        (r"/builds/(.*)", BuildHandler, {"config": config, "api": api}),
        (r"/deploy/", DeployHandler, {"config": config, 
                                      "loader": loader}),
        (r"/static/(.*)", StaticFileHandler, {"path": "static/"}),
        (r"/(favicon.ico)", StaticFileHandler, {"path": "static/"})
    ],debug=True)

    application.listen(7070)
    application.debug = True
    tornado.ioloop.IOLoop.instance().start()
