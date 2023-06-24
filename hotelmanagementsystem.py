class hotelbill:

    def __init__(self, tot='', s=0, p=0, r=0, a=1500, name='', address='', cindate='', coutdate='', rno=1000):

        print("\n\n*****___WELCOME TO  HOTEL 5 STAR GRAND___*****\n\n")

        self.tot = tot
        self.r = r
        self.p = p
        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno

    def inputdata(self):
        self.name = input("\nENTER YOUR NAME :")
        self.cindate = input("\nEnter your checkin date:")
        self.coutdate = input("\nEnter your checkout date:")
        self.address = input("\nEnter your address:")
        print("Your room no.:", self.rno, "\n")

    def roomrent(self):

        print("We have the following rooms for you:-")

        print("1.  type --->ROYAL---->RS.10000 PN\-")

        print("2.  type --->LUXURIOUS--->RS. 6000 PN\-")

        print("3.  type --->SUPREME--->RS. 4000 PN\-")

        print("4.  type --->DELUXE--->RS. 3000 PN\-")

        x = int(input("Enter Your Choice Please(enter 1/2/3/4)--->"))

        n = int(input("ENTER THE NUMBER OF NIGHTS YOU WANT TO STAY:"))

        if (x == 1):

            print("you have opted room type -->ROYAL")

            self.s = 10000 * n

        elif (x == 2):

            print("you have opted room type -->LUXURIOUS")

            self.s = 6000 * n

        elif (x == 3):

            print("you have opted room type -->SUPREME")

            self.s = 4000 * n

        elif (x == 4):
            print("you have opted room type -->DELUXE")

            self.s = 3000 * n

        else:

            print("please choose a VALID room")

        print("your room rent is =", self.s, "\n")

   
    def display(self):
        print("******HOTEL BILL******")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check in date:", self.cindate)
        print("Check out date", self.coutdate)
        print("Room no.", self.rno)
        print("Your Room rent is:", self.s)
        print("Your Food bill is:", self.r)
        print("Your Game bill is:", self.p)

        self.tot = self.s + self.p + self.r

        print("Your sub total bill is:", self.tot)
        print("Additional Service Charges is", self.a)
        print("Your grandtotal bill is:", self.tot+ self.a, "\n")
        self.rno += 1


def main():
    a = hotelbill()

    while (1):
        print("1.Enter Customer Data")

        print("2.Calculate roomrent")

        print("3.EXIT")

        b = int(input("\nEnter your choice:"))
        if (b == 1):
            a.inputdata()

        if (b == 2):
            a.roomrent()

        if (b == 6):
            quit()


main()
