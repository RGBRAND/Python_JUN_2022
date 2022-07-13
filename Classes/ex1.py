class Fan:
    brand = 'Orient'
    blade_size = 1200
    rpm = 380

    def start(self, speed=1):
        print(f'Fan is starting at {speed} speed')

if __name__ == "__main__":
    f = Fan()
    g = Fan()

    f.start(2)
    g.start(3)
    print(f.blade_size, g.blade_size)
    print(f.rpm, g.rpm)
    print(f.brand, g.brand)

    f.blade_size = 1400
    f.brand = 'Usha'
    f.rpm = 800
    print(f.blade_size, g.blade_size)
    print(f.rpm, g.rpm)
    print(f.brand, g.brand)
    