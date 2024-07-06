import random

class Saveface:
    def __init__(self):
        self.__v = None
    
    def num(self , n):
        self.__v = n
    
    @property
    def v(self):
        return self.__v

class shakedice:
    def shake(self):
        self.__face = []
        for i in range(3):
            self.__face.append(Saveface())
        for i in range(len(self.__face)):
            self.__face[i].num(random.randint(1,6))

    def __str__(self):
        total = 0
        facedice = []
        for i in self.__face:
            facedice.append(i.v)
        if len(set(facedice)) == 1:
            total = sum(facedice) * 5
            return F"{total} ({' '.join(map(str , facedice))})"
        even = []
        for i in facedice:
            if i % 2 == 0:
                even.append(i)
        if len(even) == len(facedice) or len(even) == 0:
            total = sum(facedice) * 2
            return F"{total} ({' '.join(map(str , facedice))})"
        return F"{sum(facedice)} ({' '.join(map(str , facedice))})"

ls = shakedice()
for i in range(10):
    ls.shake()
    print(ls)
