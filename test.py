from lifxlan import *

lan = LifxLAN()
lights = lan.get_lights()
l = lights[0]
print(l.get_label())
input()
l.set_group("test")
