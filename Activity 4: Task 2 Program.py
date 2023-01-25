import random
class Enemy:
    def __init__(self):
        self.x = 0
        self.y = 0
    def spawn(self, map_width, map_height):
        self.x = random.uniform(0, map_width)
        self.y = random.uniform(0, map_height)
        print("I am at: ({}, {})".format(self.x, self.y))
enemy = Enemy()
map_width = 100
map_height = 100
enemy.spawn(map_width, map_height)
