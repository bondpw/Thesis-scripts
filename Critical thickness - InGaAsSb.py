import numpy as np

'''Physical constants, from Matthews Blakeslee and Vurgaftman'''
b = 4
a_InSb = 6.4794
c12_InSb = 373.5
c11_InSb = 684.7
a_InAs = 6.0583
c12_InAs = 452.6
c11_InAs = 832.9
a_GaSb = 6.0959
c12_GaSb = 402.6
c11_GaSb = 884.2
a_GaAs = 5.65325
c12_GaAs = 566
c11_GaAs = 1221

'''Matthews Blakeslee equation'''
def hc(b,e,v,x):
    return (b/(4*np.pi*e))*((1-(v*0.25))/((1+v)*0.5))*(np.log(x/b)+1)

'''People and Beam equation'''
def hc_pb(a,b,e,v,x):
    return ((1 - v)/(1 + v))*(1/(16 * np.sqrt(2)))*((b**2)/a)*((1/((2*e)**2)))*(np.log(x/b))

'''Fucntion which returns the critical thickness using the Matthews-Blakeslee equation for an InGaAsSb alloy with In content "In" and Sb content "Sb" on a GaSb substrate'''
def hc_ingaassb_mb(In,Sb):
    '''Indium and Antimony contents'''
    In_x = In
    Sb_y = Sb
    '''Lattice constant of defined alloy'''
    a_alloy = ((In_x * Sb_y) * a_InSb) + ((In_x * (1- Sb_y)) * a_InAs) + (((1-In_x) * Sb_y) * a_GaSb) + (((1-In_x)*(1-Sb_y)) * a_GaAs)
    '''Elastic constants of defined alloy'''
    c11_alloy =  ((In_x * Sb_y) * c11_InSb) + ((In_x * (1- Sb_y)) * c11_InAs) + (((1-In_x) * Sb_y) * c11_GaSb) + (((1-In_x)*(1-Sb_y)) * c11_GaAs)
    c12_alloy = ((In_x * Sb_y) * c12_InSb) + ((In_x * (1- Sb_y)) * c12_InAs) + (((1-In_x) * Sb_y) * c12_GaSb) + (((1-In_x)*(1-Sb_y)) * c12_GaAs)

    e = abs((a_GaSb / a_alloy) - 1)
    v = c12_alloy/(c12_alloy + c11_alloy)
    '''Caculation of the recursive critical layer thickness equation'''
    x=2
    crit = hc(b,e,v,x)
    while abs(crit-x)>0:
        x=crit
        dumcrit = hc(b,e,v,x) 
    return dumcrit  
'''Fucntion which returns the critical thickness using the People-Bean equation for an InGaAsSb alloy with In content "In" and Sb content "Sb" on a GaSb substrate'''
def hc_ingaassb_pb(In,Sb):
    '''Same formulation as in Matthews-Blakeslee solver'''
    In_x = In
    Sb_y = Sb

    a_alloy = ((In_x * Sb_y) * a_InSb) + ((In_x * (1- Sb_y)) * a_InAs) + (((1-In_x) * Sb_y) * a_GaSb) + (((1-In_x)*(1-Sb_y)) * a_GaAs)

    c11_alloy =  ((In_x * Sb_y) * c11_InSb) + ((In_x * (1- Sb_y)) * c11_InAs) + (((1-In_x) * Sb_y) * c11_GaSb) + (((1-In_x)*(1-Sb_y)) * c11_GaAs)
    c12_alloy = ((In_x * Sb_y) * c12_InSb) + ((In_x * (1- Sb_y)) * c12_InAs) + (((1-In_x) * Sb_y) * c12_GaSb) + (((1-In_x)*(1-Sb_y)) * c12_GaAs)
    ena = (a_GaSb / a_alloy) - 1
    e = abs((a_GaSb / a_alloy) - 1)
    v = c12_alloy/(c12_alloy + c11_alloy)
        
    '''Caculation of the recursive critical layer thickness equation'''
    x=10
    crit = hc_pb(a_alloy,b,e,v,x)
    while abs(crit-x)>0:
        x=crit
        dumcritpb = hc_pb(a_alloy,b,e,v,x)  
    return dumcritpb