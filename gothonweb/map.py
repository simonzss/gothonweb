#--coding:utf-8--
from random import randint
class Room(object):
    def __init__(self,name,description):
        self.name=name
        self.description=description
        self.paths={}

    def go(self,direction):
        return self.paths.get(direction,None)

    def add_paths(self,paths):
        self.paths.update(paths)

central_corridor=Room("Central Corridor","""A start place,You can 'shoot','joke'or others.""")

laser_weapon_armory=Room("Laser Weapon Armory","""Now You enter the second mission,You need
to enter 3 digits to unlock the bomb.After 10 times trying you will die. """)

the_bridge=Room("The Bridge","""The third mission,You can 'throw' or 'place' the bomb.""")

escape_pod=Room("Escape Pod","""You are in the fouth mission,You must choose a escape pod from
'1' to '5',choose a bad pod,You die.""")

the_end_winner=Room("The End Good","""You jump into right pod and escape successfully!You Won!""")

the_end_loser=Room("The End","""You jump into bad pod.You died.""")

generic_death=Room("death",["You Died.游戏内死亡","Ni Gua Le.游戏内死亡"][randint(0,1)])


escape_pod.add_paths({           #mission4
    '2':the_end_winner,
    '*':the_end_loser
})

the_bridge.add_paths({           #mission3
    'throw':generic_death,
    'place':escape_pod
})

laser_weapon_armory.add_paths({   #mission2
    '123':the_bridge,
    '*':generic_death,
    'repeat':laser_weapon_armory
})

central_corridor.add_paths({      #mission1
    'shoot':generic_death,
    'joke':laser_weapon_armory
})

START=central_corridor
GoodEnd=escape_pod