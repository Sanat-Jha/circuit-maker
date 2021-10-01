import schemdraw.elements as elm
import schemdraw
ElementDict = {
    'Triax Cable': elm.cables.Triax(),
    'Coax Cable': elm.cables.Coax(),
    'Optocoupler Compound': elm.compound.Optocoupler(),
    'Bus Connect': elm.connectors.BusConnect(),
    'Bus Line': elm.connectors.BusLine(),
    'Coax Connect': elm.connectors.CoaxConnect(),
    'DB25': elm.connectors.DB25(),
    'DB9': elm.connectors.DB9(),
    'Header': elm.connectors.Header(),
    'Jack': elm.connectors.Jack(),
    'Jumper': elm.connectors.Jumper(),
    'Ortho Lines': elm.connectors.OrthoLines(),
    'Plug': elm.connectors.Plug(),
    'Right Lines': elm.connectors.RightLines(),
    'Ic': elm.intcircuits.Ic(),
    'Ic555': elm.intcircuits.Ic555(),
    'IcDIP': elm.intcircuits.IcDIP(),
    'IcPin': elm.intcircuits.IcPin(),
    'Voltage Regulator': elm.intcircuits.VoltageRegulator(),
    'Ant': elm.legacy.ANT(),
    'Arrow Head': elm.legacy.ARROWHEAD(),
    'Arrow Lines': elm.legacy.ARROWLINE(),
    'Cap': elm.legacy.CAP(),
    'Button': elm.legacy.BUTTON(),
    'Battery': elm.legacy.BATTERY(),
    'Fuse': elm.legacy.FUSE(),
    'Inductor': elm.legacy.INDUCTOR(),
    'GND': elm.legacy.GND(),
    'LED': elm.legacy.LED(),
    'Motor': elm.legacy.MOTOR(),
    'Speaker': elm.legacy.SPEAKER(),
    'Transformer': elm.legacy.transformer(),
    'Line': elm.legacy.LINE(),
    'Switches': elm.switches.Button(),
    'Transistor': elm.transistors.BjtPnp(),
    'Battery Cell': elm.sources.BatteryCell(),
    'Lamp': elm.sources.Lamp(),
    'Meter OHM': elm.sources.MeterOhm(),
    'Solar': elm.sources.Solar(),
    'Capacitor': elm.twoterm.Capacitor(),
    'Resistor': elm.twoterm.Resistor(),
    'Diode': elm.twoterm.Diode(),
    'Inductor': elm.twoterm.Inductor(),
    'Potentiometer': elm.twoterm.Potentiometer(),
    }
def makecircuit(circuitlst):
    d = schemdraw.Drawing()
    for i in circuitlst:
        if i[2] == "":
            if i[1] == "Up":
                d.add(ElementDict[i[0]].up())
            if i[1] == "Down":
                d.add(ElementDict[i[0]].down())
            if i[1] == "Left":
                d.add(ElementDict[i[0]].left())
            if i[1] == "Right":
                d.add(ElementDict[i[0]].right())
            if i[1] == "Auto":
                d.add(ElementDict[i[0]])
        else:
            if i[1] == "Up":
                d.add(ElementDict[i[0]].up().label(i[2]))
            if i[1] == "Down":
                d.add(ElementDict[i[0]].down().label(i[2]))
            if i[1] == "Left":
                d.add(ElementDict[i[0]].left().label(i[2]))
            if i[1] == "Right":
                d.add(ElementDict[i[0]].right().label(i[2]))
            if i[1] == "Auto":
                d.add(ElementDict[i[0]].label(i[2]))
    return d.draw(show=False)
