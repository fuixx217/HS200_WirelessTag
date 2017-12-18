from pyHS100 import SmartPlug, SmartBulb
from pprint import pformat as pf

plug = SmartPlug("10.0.0.122")
print("Hardware: %s" % pf(plug.hw_info))
print("Full sysinfo: %s" % pf(plug.get_sysinfo())) # this prints lots of information about the device

plug.turn_on()
