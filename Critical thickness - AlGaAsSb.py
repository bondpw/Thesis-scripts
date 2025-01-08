import numpy as np

'''Physical constants, from Matthews Blakeslee and Vurgaftman'''
b = 4
a_GaSb = 6.0959
c12_GaSb = 402.6
c11_GaSb = 884.2
a_GaAs = 5.65325
c12_GaAs = 566
c11_GaAs = 1221
a_AlAs = 5.6611
c11_AlAs = 1250
c12_AlAs = 534
a_AlSb = 6.1355
c11_AlSb = 876.9
c12_AlSb = 434.1

'''Matthews Blakeslee equation'''
def hc(b,e,v,x):
    return (b/(4*np.pi*e))*((1-(v*0.25))/((1+v)*0.5))*(np.log(x/b)+1)

'''People and Beam equation'''
def hc_pb(a,b,e,v,x):
    return ((1 - v)/(1 + v))*(1/(16 * np.sqrt(2)))*((b**2)/a)*((1/((2*e)**2)))*(np.log(x/b))

'''Fucntion which returns the critical thickness using the Matthews-Blakeslee equation for an InGaAsSb alloy with In content "In" and Sb content "Sb" on a GaSb substrate'''
def hc_algaassb_mb(Al,Sb):
    '''Aluminium and Antimony contents'''
    Al_x = Al
    Sb_y = Sb
    '''Lattice constant of defined alloy'''
    a_alloy = ((Al_x * Sb_y) * a_AlSb) + ((Al_x * (1- Sb_y)) * a_AlAs) + (((1-Al_x) * Sb_y) * a_GaSb) + (((1-Al_x)*(1-Sb_y)) * a_GaAs)
    '''Elastic constants of defined alloy'''
    c11_alloy =  ((Al_x * Sb_y) * c11_AlSb) + ((Al_x * (1- Sb_y)) * c11_AlAs) + (((1-Al_x) * Sb_y) * c11_GaSb) + (((1-Al_x)*(1-Sb_y)) * c11_GaAs)
    c12_alloy = ((Al_x * Sb_y) * c12_AlSb) + ((Al_x * (1- Sb_y)) * c12_AlAs) + (((1-Al_x) * Sb_y) * c12_GaSb) + (((1-Al_x)*(1-Sb_y)) * c12_GaAs)

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
def hc_ingaassb_pb(Al,Sb):
    '''Same formulation as in Matthews-Blakeslee solver'''
    '''Aluminium and Antimony contents'''
    Al_x = Al
    Sb_y = Sb
    '''Lattice constant of defined alloy'''
    a_alloy = ((Al_x * Sb_y) * a_AlSb) + ((Al_x * (1- Sb_y)) * a_AlAs) + (((1-Al_x) * Sb_y) * a_GaSb) + (((1-Al_x)*(1-Sb_y)) * a_GaAs)
    '''Elastic constants of defined alloy'''
    c11_alloy =  ((Al_x * Sb_y) * c11_AlSb) + ((Al_x * (1- Sb_y)) * c11_AlAs) + (((1-Al_x) * Sb_y) * c11_GaSb) + (((1-Al_x)*(1-Sb_y)) * c11_GaAs)
    c12_alloy = ((Al_x * Sb_y) * c12_AlSb) + ((Al_x * (1- Sb_y)) * c12_AlAs) + (((1-Al_x) * Sb_y) * c12_GaSb) + (((1-Al_x)*(1-Sb_y)) * c12_GaAs)

    e = abs((a_GaSb / a_alloy) - 1)
    v = c12_alloy/(c12_alloy + c11_alloy)
    '''Caculation of the recursive critical layer thickness equation'''
        
    '''Caculation of the recursive critical layer thickness equation'''
    x=10
    crit = hc_pb(a_alloy,b,e,v,x)
    while abs(crit-x)>0:
        x=crit
        dumcritpb = hc_pb(a_alloy,b,e,v,x)  
    return dumcritpb