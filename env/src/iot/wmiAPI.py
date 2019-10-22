import os
import re

def getCPUTemperature():
    out = os.popen('wmic /namespace:\\\\root\wmi PATH MSAcpi_ThermalZoneTemperature get CriticalTripPoint, CurrentTemperature').read()
    x = re.findall("\\d{1,}", out)
    return float(x[1])/10 - 273.15
