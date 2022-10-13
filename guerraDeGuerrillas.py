import numpy as np

def getAttackUnities():
        np.random.seed(0)
        maxAttackStrength = 10
        sumStrengthAttack = 0
        attackUnities = dict()
        while sumStrengthAttack < maxAttackStrength:
                while sumStrengthAttack > maxAttackStrength:
                        strengthAttack = np.random.randint(1, maxAttackStrength+1)
                        attackUnities[strengthAttack] = strengthAttack


        return attackUnities

print(getAttackUnities())