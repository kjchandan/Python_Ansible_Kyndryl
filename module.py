def fun():
    """
    Simple Python function
    to demonstrate modules 
    """
    print("Learning Python is fun")

    total = lambda a=0, b=0, *args, **kwargs:a + b + sum(args) + sum(kwargs.values())