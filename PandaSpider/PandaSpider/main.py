import os
from scrapy.cmdline import execute
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
execute(["scrapy","crawl","Panda"])