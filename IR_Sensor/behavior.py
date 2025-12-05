from wokwi_api import *

out_pin = None

def on_start(sim):
    global out_pin
    out_pin = sim.pin("OUT")
    out_pin.set_level(0)

def on_tick(sim):
    t = sim.millis()
    if (t // 1000) % 2 == 0:
        out_pin.set_level(1)
    else:
        out_pin.set_level(0)
