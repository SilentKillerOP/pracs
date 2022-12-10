def NumGame(n):
    x = int(input("Enter num: "))

    try:
        if x < n:
            raise LowerNumber
        elif x > n:
            raise GreaterNumber
    except Exception as e:
        print(e)
        NumGame(n)
    else:
        print("You got number right")


class LowerNumber(Exception):
    def __str__ (self):
        return "Number is Lower"

class GreaterNumber(Exception):
    def __str__ (self):
        return "Number is Greater"

NumGame(20)