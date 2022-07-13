#constractor

class Paratha:

    def __init__(self, typ, price):
        self.type = typ
        self.price = price

    def display(self):
        print(f"{self.type} : {self.price}")

if __name__ == "__main__":
        ap = Paratha("Aloo Paratha", 80)
        bp = Paratha("Panner Paratha",120)
        pp = Paratha("Pyaaz Paratha",60)
        mp = Paratha("Muli Paratha",70)

        print("Today's Menu")
        ap.display()
        bp.display()
        pp.display()
        mp.display()

    
