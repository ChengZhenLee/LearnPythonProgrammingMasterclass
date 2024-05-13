class Wing(object):
    
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I thin I'll just walk")


class Duck(object):

    def __init__(self):
        # Create a Wing object and assign to the _wing attribute of the duck class
        # This is called a Composition
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")
    
    def quack(self):
        print("Are you 'avin a larf? I'm a penguin!")

    
# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

class Flock(object):
    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        self.flock.append(duck)
    
    def migrate(self):
        for duck in self.flock:
            try:
                duck.fly()
            # exception is stored in a variable e
            except AttributeError as e:
                print("One duck down")
                problem = e
                # raise
                
        # Only raises the error once the for loop is done
        if problem:
            # 'raise' claus raises an error in the program
            raise problem
    

if __name__ == '__main__':
    donald = Duck()
    donald.fly()

    # percy = Penguin()
    # test_duck(percy)