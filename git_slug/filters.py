"Custom filters for Jinja2 templates"
import time

def localtime(seconds):
    "Create time tuple in local time from seconds since epcoh"
    return time.localtime(seconds)

def gmtime(seconds):
    "Create time tuple in UTX time from seconds since epoch"
    return time.gmtime(seconds)

def tsformat(tstamp, format="%a %b %d %H:%M:%S %Y"):
    "Format time tuple as string"
    return time.strftime(format, tstamp)
