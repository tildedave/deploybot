from fabric.api import run

def uname():
    run('uname -a')

def install(build, comment):
    uname()
    print("We should install the build %s!" % build)
