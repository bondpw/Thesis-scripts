'''Lattice constants of binary alloys'''
aInAs = 6.0583
aInSb = 6.4794
aGaSb = 6.0959

'''Strain of InAs on GaSb'''
eInAs = (aGaSb/aInAs)-1

'''A function which returns how many monolayers of InAsSb of antimony content Sb_x are requred to create a strain balanced system with InAs monolayers of InAs_n'''
def InAsSb_MLs(InAs_n,Sb_x):
    '''lattice constant of specific InAsSb'''
    aInAsSbx = ((1-Sb_x)*aInAs)+(Sb_x*aInSb)
    '''Strain of InAsSb on GaSb'''
    eInAsSb = (aGaSb/aInAsSbx)-1
    '''Strain ratio of InAs to InAsSb'''
    SR = abs(eInAs/eInAsSb)

    return  SR * InAs_n