class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    pass


class E(B, C):
    pass

class G:
    pass

class F(G, E,D):
    pass

f = F()
print(f.d())
print(F.mro())