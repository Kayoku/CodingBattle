import math

v = int(input())
va = int(input())
vb = int(input())

def ta(va, vb):
    n_va, n_vb = (va*va*va, vb*vb)
    v2 = n_va + n_vb
    return (v2, n_va, n_vb)

def tb(va, vb):
    n_va, n_vb = (va*va, vb*vb*vb)
    v2 = n_va + n_vb
    return (v2, n_va, n_vb)

def diminue(va, vb):
    n_va, n_vb = int(math.sqrt(va)), int(math.sqrt(va))
    v2 = n_va + n_vb
    return (v2, n_va, n_vb)


def greedy(va, vb):
    v_ta, va_ta, vb_ta = ta(va, vb)
    v_tb, va_tb, vb_tb = tb(va, vb)

    print(str(v_ta) + " " + str(v_tb))
    
    if v_ta < v:
        if v_ta > v_tb:
            return greedy(va_ta, vb_ta)
        elif v_tb < v:
            return greedy(va_tb, vb_tb)
        return greedy(va_ta, vb_ta)

    if v_tb < v:
        if v_tb > v_ta:
            return greedy(va_tb, vb_tb)
        elif v_ta < v:
            return greedy(va_ta, vb_ta)
        return greedy(va_tb, vb_tb)
    return va + vb

print(greedy(va, vb))
        
    
    
    
