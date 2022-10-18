from math import floor
from math import pi

def deg_to_gms(degrees):
    full_degrees = floor(degrees)
    ost = (degrees - full_degrees) *60
    full_minutes = floor(ost)
    full_seconds = round(ost % 1, 2)
    returnable = str(f"{full_degrees}* {full_minutes}' {full_seconds}''")
    return returnable

def gms_to_deg(deg, min, sec):
    full = deg*3600 + min*60 + sec
    full = full / 3600
    return full

def deg_to_rad(deg):
    return (deg*pi)/180

def rad_to_deg(rad):
    return (rad*180)/pi
print(deg_to_gms(36.97))
print(gms_to_deg(36, 58, 0.2))
print(rad_to_deg(deg_to_rad(163)))
