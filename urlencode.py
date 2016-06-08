import sys
import urllib

script={"query":sys.argv[1]}

print urllib.urlencode(script)
