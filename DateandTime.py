class Date:
    def __init__(self, dd, mm, yy):
        self.dd, self.mm, self.yy = dd, mm, yy

    def display(self):
        print(self.dd, self.mm, self.yy)

    def __add__(self, days):
        temp=Date(self.dd, self.mm, self.yy)
        temp.dd += days

        while temp.dd > 28:
            if temp.dd > 28 and temp.mm == 2 and temp.yy % 4 :
                temp.dd -= 28
                temp.mm +=1
            if temp.dd > 29 and temp.mm == 2 and temp.yy % 4 == 0:
                temp.dd -= 29
                temp.mm += 1
            elif temp.dd > 31 and temp.mm in (1,3,5,7,8,10,12):
                temp.dd -= 31
                temp.mm += 1
                if temp.mm == 13:
                    temp.mm = 1
                    temp.yy +=1
                    
            elif temp.dd > 30 and temp.mm in (4,6,9,11):
                temp.dd -= 30
                temp.mm += 1
            else:
                break
        return temp
    

        # if temp.dd > 28 and temp.mm == 2:
        #     temp.dd -= 28
        #     temp.mm += 1
        # if temp.dd > 31 and temp.mm == 3:
        #     temp.dd -= 31
        #     temp.mm += 1
        # if temp.dd > 30 and temp.mm ==4:
        #     temp.dd -= 30
        #     temp.mm += 1
        # return temp
    
    
# ---------------------

# today=Date(28, 2, 2025)
# today.display()
# tomorrow = today + (365 * 4 + 47)
# tomorrow.display()
# print(id(today))
# print(id(tomorrow))

    def __strr__(self):
        print("In __str__")
        return str(self.dd)+"/"+str(self.mm)+"/"+str(self.yy)

    def __repr__(self):
        return str(self.dd)+"/"+str(self.mm)+"/"+str(self.yy)

today=Date(13,2,2025)
tomorrow = today + 47
print(tomorrow)
print(dir(today))
print(dir(Date))