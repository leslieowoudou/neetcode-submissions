import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self,length:int, width :int =None)->float:
        area=0
        if width==None:
            area=(math.pi)*length*length
            area=round(area,2)
        else:
            area=length * width

        return area

        

    
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
