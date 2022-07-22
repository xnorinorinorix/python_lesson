
class Square:
    square_list=[]

    def __init__(self, length) -> None:
        self.square_list.append(self)
        self.length = length

    def __repr__(self):
        lg = self.length
        return "{} by {} by {} by {}".format(lg, lg, lg, lg)

    def comp(self, a, b):
        return a is b


# sq = Square()
# print(sq.square_list)
# sq2 = Square()
# print(sq2.square_list)

# print(Square(29))

a = Square(29)
print(a)
print(a.comp("omg", "ppa"))
print(a.comp("equ", "equ"))


