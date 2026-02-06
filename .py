def alpha(ref):
    print("inside alpha")
    ref()

def beta():
    print("inside bata")
alpha(beta)
