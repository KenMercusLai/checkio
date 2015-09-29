def simplify(expr):
    return expr

if __name__ == "__main__": # pragma: no cover
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert simplify("(x-1)*(x+1)") == "x**2-1", "First and simple"
    assert simplify("(x+1)*(x+1)") == "x**2+2*x+1", "Almost the same"
    assert simplify("(x+3)*x*2-x*x") == "x**2+6*x", "Different operations"
    assert simplify("x+x*x+x*x*x") == "x**3+x**2+x", "Don't forget about order"
    assert simplify("(2*x+3)*2-x+x*x*x*x") == "x**4+3*x+6", "All together"
    assert simplify("x*x-(x-1)*(x+1)-1") == "0", "Zero"
    assert simplify("5-5-x") == "-x", "Negative C1"
    assert simplify("x*x*x-x*x*x-1") == "-1", "Negative C0"

