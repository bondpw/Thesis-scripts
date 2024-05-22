import numpy as np
import matplotlib.pyplot as plt

'''The range of Sb contents to be scanned over (first two in list)'''
x = np.linspace(0.1,0.2,11)
'''Lattice constants of materials'''
aInAs = 6.0584
aInSb = 6.4794
aGaSb = 6.0959

'''Strain of InAs on GaSb'''
eInAs = (aGaSb/aInAs)-1

'''Range of InAs MLs to be scanned over'''
InAsML = np.linspace(1,15,100)

'''A list of lists for the resultant InAsSb MLs from respective InAs and Sb contents'''
InAsSbMLlist = [ [] for j in range(len(x))]

'''A double list scanning over (i) for Sb content, (j) for InAs monolayers'''
for i in range(len(x)):
    '''Setting the Sb content'''
    xdum = x[i]
    '''lattice constant of specific InAsSb'''
    aInAsSbx = ((1-xdum)*aInAs)+(xdum*aInSb)
    '''Strain of InAsSb on GaSb'''
    eInAsSb = (aGaSb/aInAsSbx)-1
    '''Strain ratio of InAs to InAsSb'''
    SR = abs(eInAs/eInAsSb)
    for j in range(len(InAsML)):
        '''number of InAsSb MLs for a given amount of InAs MLs'''
        InAsSbML = SR * InAsML[j]
        InAsSbMLlist[i].append(InAsSbML)

'''loop for plotting data'''
for i in range(len(InAsSbMLlist)):
    plt.plot(InAsML,InAsSbMLlist[i], label = "x = "+str(float('%.3g' % x[i])))
plt.xlabel("InAs monolayers")
plt.ylabel("$InAsSb_{x}$ monolayers")
plt.legend(loc = "lower right")
plt.show()

    