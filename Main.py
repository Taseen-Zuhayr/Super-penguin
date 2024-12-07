class student :
    def init (self):
        print("who scored 1st mark?")
    def who(self):
        print("Vedanshi is first !!! ")
    def aboutgirl(self):
        print("vedanshi is a good girl!")

class update(student) :
    def init_(self):
        super() .__init__()
        print("who scored 1st mark 1yr later?")
    def who(self):
        print("Tasheen is first !! ")
    def about(self):
        print("Tasheen is a good boy !! ")



details = update()
details.who()
details.about()
details.aboutgirl()


