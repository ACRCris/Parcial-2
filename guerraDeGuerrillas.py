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


def  getAttackUnitiesN(attackUnities, maxAttackStrength = 10000):
        raise NotImplementedError

def getAttackUnity(attackUnities, maxAttackStrength = 10000):
        np.random.seed(1)
        labelsAttackUnities = np.array(list(attackUnities.keys()))
        probablity = np.random.rand()*maxAttackStrength
        for i in range(len(labelsAttackUnities)):
                labela = labelsAttackUnities[i-1] if i-1>=0  else 0
                label = labelsAttackUnities[i]
                leftVal = attackUnities[labela] if labela != 0 else 0
                rightVal = attackUnities[label] + leftVal
                if (probablity < rightVal) and probablity > leftVal:
                        return label, attackUnities.get(label)

                

