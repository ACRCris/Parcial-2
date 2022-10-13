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
        labeli = getAttackUnity(attackUnities, maxAttackStrength)
        probabilityV = np.random.rand()
        if(labeli == 1 or probabilityV <= umbralV):
                labelj = getAttackUnity(attackUnities, maxAttackStrength)
                
                while labelj == labeli:
                        labelj = getAttackUnity(attackUnities, maxAttackStrength)

                attackUnities = fusionAttackUnity(labeli, labelj, attackUnities)
        elif(probabilityV > umbralV or labeli == maxAttackStrength):
                attackUnities = fissionAttackUnity(labeli, attackUnities)

        return attackUnities

                

def getAttackUnity(attackUnities, maxAttackStrength = 10000):
        #np.random.seed(seed)
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
        print("fusionAttackUnity", labeli, labelj)
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

print(getAttackUnities0()[0])
for i in range(100):
        print(i, getAttackUnitiesN(getAttackUnities0()[0],i,umbralV = 0.5))

