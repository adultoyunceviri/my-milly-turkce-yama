init python:
        class Attributes:
            def __init__(self, character, friendship=0, love=0):
                self.character = character
                self.friendship = friendship
                self.love = love

            def set_friendship(self, value):
                self.friendship = self.friendship + value

            def get_friendship(self):
                return self.friendship

            def set_love(self, value):
                self.love = self.love + value

            def get_love(self):
                return self.love

        woman_name = "Woman"
        man_name = "Man"

# Define Characters
define mc = Character("[mc]", color="#00A0E3", dynamic=True)
define ml = Character("Milly", color="#EFC6E1")
define ld = Character("Linda", color="#EFC6E1")
define nce = Character("Nicole", color="#EFC6E1")
define sop = Character("Sophia", color="#EFC6E1")

# Default Value
default MC = "Josh"

# Shortcuts
define ML = ml.name
define LD = ld.name
define NCE = nce.name
define SOP = sop.name

# Answer
define D01_answ1 = False
define D01_answ2 = False
define D01_answ3 = False
define D01_answ4 = False
define D01_answ5 = False
define D01_answ6 = False

define flash = Fade(.25, 0, .2, color="#fff")

label start:

$ ml_attr = Attributes('ml', 0, 0)
$ ld_attr = Attributes('ld', 0, 0)
$ nce_attr = Attributes('nce', 0, 0)
$ sop_attr = Attributes('sop', 0, 0)

define Linda = False

label begin:
    jump intro
    jump begin3

label after_load:
    if not Linda:
        $ Linda = False
