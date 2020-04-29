class ArbreBianire :
    def __init__(self):
        self.left = None
        self.right = None
        self.data = 0

    def getRightNode(self):
        return(self.right)
            
    def getLeftNode(self):
        return(self.left)

    def setValue(self, newValue):
        self.data = newValue

    def getValue(self):
        return(self.data)

    def str(self):
        return("Noeud actuel : " + str(self.data) + ";\nNoeud de droite : " + str(self.right.data) + ";\nNoeud de gauche : " + str(self.left.data) + ";")

    def Postfixe(self):
        pstfxLeft = []
        pstfxRight = []
        finalStr = ""
        Test = self.left
        cmpt = 0
        while(Test):
            cmpt += 1
            if(cmpt % 2 == 0):
                pstfxLeft.append(str(Test.data))
                Test = Test.left
            else:
                if(Test.right):
                    pstfxLeft.append(str(Test.right.data))
                else:
                    pass

        Test = self.right
        cmpt = 0
        while(Test):
            cmpt += 1
            if(cmpt % 2 == 0):
                pstfxRight.append(str(Test.data))
                Test = Test.right
            else: 
                if(Test.left):
                    pstfxRight.append(str(Test.left.data))
                else:
                    pass

        for i in pstfxLeft :
            finalStr += str(i) + " , "

        for i in pstfxRight :
            finalStr += str(i) + " , "
        
        finalStr += str(self.data)
        return("Postfixe : " + finalStr)

    def Prefixe(self):
        prefxLeft = []
        prefxRight = []
        finalStr = str(self.data)
        Test = self.left
        cmpt = 0
        while(Test):
            cmpt += 1
            if(cmpt % 2 == 1):
                prefxLeft.append(str(Test.data))
                Test = Test.left
            else:
                if(Test.right):
                    prefxLeft.append(str(Test.right.data))
                else:
                    pass

        Test = self.right
        cmpt = 0
        while(Test):
            cmpt += 1
            if(cmpt % 2 == 0):
                prefxRight.append(str(Test.data))
                Test = Test.right
            else: 
                if(Test.left):
                    prefxRight.append(str(Test.left.data))
                else:
                    pass
        print(prefxLeft)
        for i in prefxLeft[::-1] :
            finalStr += " , " + str(i)

        for i in prefxRight[::-1] :
            finalStr += " , " + str(i)
        
        return("Préfixe : " + finalStr)

    def Infixe(self):
        infxLeft = []
        infxRight = []
        finalStr = ""
        Test = self.left
        cmpt = 0
        while(Test):
            cmpt += 1
            if(cmpt % 2 == 0):
                infxLeft.append(str(Test.data))
                Test = Test.left
            else:
                if(Test.right):
                    infxLeft.append(str(Test.right.data))
                else:
                    pass

        Test = self.right
        cmpt = 0
        while(Test):
            cmpt += 1
            if(cmpt % 2 == 0):
                infxRight.append(str(Test.data))
                Test = Test.right
            else: 
                if(Test.left):
                    infxRight.append(str(Test.left.data))
                else:
                    pass

        for i in infxLeft[::-1] :
            finalStr += str(i) + " , "

        finalStr += str(self.data)

        for i in infxRight :
            finalStr += " , " + str(i)
        
        return("Infixe : " + finalStr)

class TestArbreBinaire :
    
    abr = ArbreBianire()
    abr.data = 45
    abr.left = ArbreBianire()
    abr.left.data = 39
    abr.right = ArbreBianire()
    abr.right.data = 48
    abr.left.left = ArbreBianire()
    abr.left.left.data = 14
    abr.left.right = ArbreBianire()
    abr.left.right.data = 41
    abr.left.left.right = ArbreBianire()
    abr.left.left.right.data = 17    

    # print(abr.Postfixe())    
    print(abr.Prefixe())    
    # print(abr.Infixe())


# Pré  = 19 11 3 21
# Post = 3 11 21 19
# Inf  = 3 11 19 21


# [5]
# Pré  = 45 39 14 17 41 48
# Post = 17 14 41 39 48 45
# Inf  = 14 17 39 41 45 48