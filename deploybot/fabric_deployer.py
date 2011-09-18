#!/usr/bin/python2.5

import subprocess

class FabricDeployer:

    def __init__(self, fabric_opts):
        self.fabric_opts = fabric_opts

    def deploy(self, build, log):
        print "Launching, outputting to %s" % (log)

        logfile = file(log, "w")

        argitems = self.fabric_opts["arguments"].items()
        argstring = ",".join(["%s=%s" % (k,i) for k,i in argitems])

        fabric_command = [ "fab", "-H", 
                           ",".join(self.fabric_opts["hosts"]),
                           "-u",
                           self.fabric_opts["username"],
                           "-p",
                           self.fabric_opts["password"],
                           "-f",
                           self.fabric_opts["fabfile"],
                           "install:build=%s,%s" % (build,argstring) ]

        print fabric_command

        p = subprocess.Popen(fabric_command,
                             stdout=logfile,
                             stderr=logfile,
                             close_fds=True)
        p.communicate()
        return p.returncode
