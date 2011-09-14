#!/usr/bin/python2.5

# From http://www.voidspace.org.uk/python/mock/examples.html#matching-any-argument-in-assertions

class _ANY(object):
     def __eq__(self, other):
         return True

ANY = _ANY()
