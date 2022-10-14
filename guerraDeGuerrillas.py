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
        attackUnities = deleteAttackUnity(labeli, attackUnities)
        probabilityV = np.random.rand()
        if(labeli == 1 or (probabilityV > umbralV and labeli != maxAttackStrength)):
                labelj = getAttackUnity(attackUnities,seed+2, maxAttackStrength)
                attackUnities = deleteAttackUnity(labelj, attackUnities)
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
        if(len(labelsAttackUnities) > 1):
                for i in range(len(labelsAttackUnities)):
                        #labela = labelsAttackUnities[i-1] if i-1>=0  else 0
                        label = labelsAttackUnities[i]
                        leftVal = rightVal
                        rightVal = attackUnities[label] + leftVal
                        if (probablityP < rightVal) and probablityP >= leftVal:
                                return label
        else:
                return labelsAttackUnities[0]



def fusionAttackUnity(labeli, labelj, attackUnities):
        if(attackUnities.get(labeli+labelj) == None):
                attackUnities[labeli+labelj] = labeli+labelj
        else:
                attackUnities[labeli+labelj] += labeli+labelj

        return attackUnities

def fissionAttackUnity(label, attackUnities):
        if(attackUnities.get(1) == None):
                attackUnities[1] = label
        else:
                attackUnities[1] += label

        return attackUnities

def deleteAttackUnity(label, attackUnities):
        if(attackUnities[label] == label):
                attackUnities.pop(label)
        else:
                attackUnities[label] -= label

        return attackUnities

#print(getAttackUnities0()[0])
#attactUnities = getAttackUnitiesN({10000:10000},1,umbralV = 0.01)
#print(attactUnities)
#for i in range(10000):
#        attactUnities = getAttackUnitiesN(attactUnities,i,umbralV = 0.01)
#        print(i,attactUnities)

attactUnities = getAttackUnitiesN({1: 4339, 2: 1642, 3: 996, 4: 456, 5: 400, 6: 306, 7: 259, 8: 176, 9: 90, 13: 65, 10: 100, 14: 56, 11: 132, 17: 34, 12: 24, 16: 112, 18: 90, 20: 40, 23: 69, 15: 45, 33: 99, 26: 26, 21: 21, 24: 24, 31: 31, 19: 38, 90: 90, 50: 50, 45: 45, 46: 46, 35: 35, 39: 39, 25: 25} ,4167,umbralV = 0.01)
#print(attactUnities)