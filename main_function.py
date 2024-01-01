from numba import  jit

@jit(nopython=True)
def main(massege):
    l = [i**3 for i in range(massege)]
    print(l)
