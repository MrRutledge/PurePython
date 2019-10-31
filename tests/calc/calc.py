# add function 

def add(a,b):
    """Add function"""
    return a + b

#subtract
def sub(a,b):
    """Subtract function"""
    return a - b

#multiply
def mult(a,b):
    """Multiply function"""
    return a * b

#division 
def div(a,b):
    """Dvivsion function"""
    if b==0:
        raise ValueError('Cannot divide by zero')
    
    return a/b