class UDE(ZeroDivisionError):
    pass

lst = [0,1,2]
ctr = 1
dct={1:1}
while ctr != -1:
    try:
        ctr = int(input("Enter a number (-1 to exit) :  "))
        if ctr == 5:
            raise ZeroDivisionError
        elif ctr==2: ctr.int
        elif ctr==3: lst[ctr]
        elif ctr==4: dct[ctr]
        elif ctr==5: import ctr
        elif ctr==6: m[ctr]
        elif ctr==7: raise KeyboardInterrupt
        elif ctr==8: raise UDE
        elif ctr==9: raise SystemExit
    except KeyboardInterrupt:
        print("KeyboardInterrupt")

    except ValueError:
        print("That as not  number")
    except Exception as e:
        print("Value of e")
        print("st(type(e))", str(type(e)))
        exception_type = str(type(e))[8:-2]
        print(exception_type)
    # else:
    #     print("There are no exceptions")
    # finally:
    #     print("Finally : gets executed all the time")