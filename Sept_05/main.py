ls = [1,4,'ajajaj', (7,8)]
try:
    i = ls.index(4)
    print(i)
except:
    print("no")

tp = (1,4,'ajajaj', (7,8), 56,899)


class auto:
    def __init__ (self, cur_fuel, engine ): # конструктор
        self.mcur_fuel = cur_fuel
        self.mengine = engine
    def rashod(self, dist):
        self.mcur_fuel -= dist/10.
        if self.mcur_fuel < 0.:
            raise Exception('pipec')
au = auto (10,1)
try:
    au.rashod(1000)
except:
    print('except')

   # au.rashod(1000)

