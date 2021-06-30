#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/opt/geoapp/geoapp")

from geoapp import app as application
