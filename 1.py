def Decorator(a):
    def f(v0,v,t):
        a(v0,v,t)
        s=(v**2 - v0**2)/(2*((v-v0)/t))
        print(s)
    return f

@Decorator
def a(v0,v,t):
    a=(v-v0)/t
    print(a)

try:
    v0=int(input('v0'))
    v=int(input('v'))
    t=int(input('t'))
    a(v0,v,t)
except ZeroDivisionError:
    print('time must be > 0')
except ValueError:
    print('Числа вводи')