# Let's try this shit
scene1 = "Oh, Starting the game, everything is new and beautiful"

class Scenes(object):

    def __init__(self, scene):
        self.scene = scene

    def print_scene(self):
        print(self.scene)

scene = Scenes(scene1)
scene.print_scene()
