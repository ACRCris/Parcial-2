from distutils.command.config import LANG_EXT
import numpy as np

def getAttackUnities0():

        np.random.seed(1)
        maxAttackStrength = 10000
        sumStrengthAttack = 0

        attackUnities = dict()
        while sumStrengthAttack != maxAttackStrength:
                strengthAttack = np.random.randint(1, maxAttackStrength+1)
                sumStrengthAttack += strengthAttack
                while sumStrengthAttack > maxAttackStrength:
                        sumStrengthAttack -= strengthAttack
                        strengthAttack = np.random.randint(1, maxAttackStrength+1)
                        sumStrengthAttack += strengthAttack

                if(attackUnities.get(strengthAttack) == None):
                        attackUnities[strengthAttack] = strengthAttack
                else:
                        attackUnities[strengthAttack] += strengthAttack

        
        return attackUnities, sumStrengthAttack


def  getAttackUnitiesN(attackUnities,seed, maxAttackStrength = 10000, umbralV = 0.01):
        np.random.seed(seed)
        labeli = getAttackUnity(attackUnities,seed +1 , maxAttackStrength)
        probabilityV = np.random.rand()
        if(labeli == 1 or (probabilityV > umbralV and labeli != maxAttackStrength)):
                labelj = getAttackUnity(attackUnities,seed+2, maxAttackStrength)
                
                while labelj + labeli> maxAttackStrength:
                        labelj = getAttackUnity(attackUnities,seed+2, maxAttackStrength)

                attackUnities = fusionAttackUnity(labeli, labelj, attackUnities)
        elif((probabilityV <= umbralV and labeli != 1) or labeli == maxAttackStrength):
                attackUnities = fissionAttackUnity(labeli, attackUnities)

        return attackUnities

                

def getAttackUnity(attackUnities, seed,maxAttackStrength = 10000):
        np.random.seed(seed)
        labelsAttackUnities = np.array(list(attackUnities.keys()))
        probablityP = np.random.rand()*maxAttackStrength
        rightVal = 0
        for i in range(len(labelsAttackUnities)):
                #labela = labelsAttackUnities[i-1] if i-1>=0  else 0
                label = labelsAttackUnities[i]
                leftVal = rightVal
                rightVal = attackUnities[label] + leftVal
                if (probablityP < rightVal) and probablityP >= leftVal:
                        return label



def fusionAttackUnity(labeli, labelj, attackUnities):
        if(attackUnities[labeli] == labeli):
                attackUnities.pop(labeli)
        else:
                attackUnities[labeli] -= labeli

        if(attackUnities[labelj] == labelj):
                attackUnities.pop(labelj)
        else:
                attackUnities[labelj] -= labelj

        if(attackUnities.get(labeli+labelj) == None):
                attackUnities[labeli+labelj] = labeli+labelj
        else:
                attackUnities[labeli+labelj] += labeli+labelj

        return attackUnities

def fissionAttackUnity(label, attackUnities):
        if(attackUnities[label] == label):
                attackUnities.pop(label)
        else:
                attackUnities[label] -= label

        if(attackUnities.get(1) == None):
                attackUnities[1] = label
        else:
                attackUnities[1] += label

        return attackUnities

#print(getAttackUnities0()[0])
#attactUnities = getAttackUnitiesN({10000:10000},1,umbralV = 0.01)
#print(attactUnities)
#for i in range(10000):
#        attactUnities = getAttackUnitiesN(attactUnities,1,umbralV = 0.01)
#        print(i,attactUnities)

attactUnities = getAttackUnitiesN({1: 4359, 1491: 1491, 1821: 1821, 2329: 2329},1,umbralV = 0.01)
