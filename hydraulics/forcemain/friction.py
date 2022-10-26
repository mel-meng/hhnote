import math
import os
import pandas as pd
def manning_sf(n, R, V):
    return (n/1.49)**2*V**2/R**(4/3)

def hw_sf(C, R, V):
    return 0.6*(V/C)**1.852/R**1.167

def dw_sf(f, V, R):
    return f*V**2/8/32.2/R


def full_pipe_vr(q, d):
    """full pipe flow, velocity and hydraulic radius


    Args:
        q (float): flow (cfs)
        d (float): diameter (ft)
        l (float): length (ft)
        s (float): slope (ft/ft)
    Returns:
        tuple: V, R
        V (float): velocity
        R (float): hydraulic radius
    """
    a = math.pi*(d/2.0)**2 # area sf
    pm = math.pi*d # perimeter ft
    R = a/pm # hydraulic radius ft
    V = q/a # velocity ft/sec
    return V, R

def get_r(r, h):
    """calculate hydraulic radius for circular pipe
    https://www.omnicalculator.com/physics/hydraulic-radius

    Args:
        r (_type_): radius
        h (_type_): water height

    Returns:
        float: hydraulic radius
    """
    if h==0:
        return 0
    theta = 2*math.acos((r-h)/r)
    A = r**2*(theta - math.sin(theta))/2
    P = r*theta
    R = A/P
    return R


VISCOS = 1.1e-5 # kinematic viscosity of water @20 deg c (sq ft/sec)

def get_re(hrad, v):
    return 4.0 * hrad * v / VISCOS

def get_fricfactor(e, hrad, re):
    """
//
//  Input:   e = roughness height (ft)
//           hrad = hydraulic radius (ft)
//           re = Reynolds number
//  Output:  returns a Darcy-Weisbach friction factor
//  Purpose: computes the Darcy-Weisbach friction factor for a force main
//           using the Swamee and Jain approximation to the Colebrook-White
//           equation.
//

    Returns:
        _type_: _description_
    """
    if ( re < 10.0 ):
        re = 10.0
    if ( re <= 2000.0 ): #laminar
        f = 64.0 / re
    else:
        if ( re < 4000.0 ): #transition, linearly interpolate between 2000 to 4000 
            f = get_fricfactor(e, hrad, 4000.0)
            f = 0.032 + (f - 0.032) * ( re - 2000.0) / 2000.0
    
        else: # turbulent
            f = e/3.7/(4.0*hrad)
            if ( re < 1.0e10 ):
                 f += 5.74/(re**0.9)
            f = math.log10(f)
            f = 0.25 / f / f
    
    return f

