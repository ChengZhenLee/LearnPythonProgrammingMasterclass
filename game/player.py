class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives
    
    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0
    
    def _get_level(self):
        return self._level
    
    def _set_level(self, level):
        if level > 0:
            delta = level - self.level
            self.score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1")

    # Properties
    # The first two parameters of the property() function is 
    # a get method and a set method
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    # Alternate way to make properties
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score

    # Provides the class with a string attribute
    # Can print the object directly and it will show this string
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0.score}".format(self)