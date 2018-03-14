from MainRoom import LockerRoom
from MainRoom import Room
from inventory import Inventory
from inventory import Item
from inventory import Literature
from inventory import LightSource
from inventory import Flashlight

room2 = Room('Room2', 'you are in the second room of the space station', 'r2')
room1 = Room('room 1', 'You are in game room of the space station', 'r1')
meetingroom = Room('meetingroom', 'You are in the meeting room ', 'mr')
bedroom1 = Room('bedroom', 'you are in a bedroom you can take a break astronaut (there is a flashlight here)', 'b1')
room3 = Room('laboratory' , 'You are in the laboratory. ', 'r3')
room4 = LockerRoom('xeno', 'You are in the last room, but there is a xenomorph', 'r4')

room2.add_connection(room3, "passage ", ["east","e"])
room2.add_connection(bedroom1, "passage ", ["west","w"])
meetingroom.add_connection(room3, "passage ", ["south", "s"])
room3.add_connection(room2, "tunel ", ["west", "w"])
room2.add_connection(room1, "door ", ["north","n"])
bedroom1.add_connection(room4, "a tiny door ", ["south west", "sw"])

room1.add_room('s', room2)
room1.add_room('e', meetingroom)

bedroom1.add_item(Flashlight())

inventory = Inventory()
current_room = room2

while True:
    current_room.enter_room(inventory)
    command = raw_input("what would you like to do? ")
    if command in ["exit", "x", "quit", "q"]:
        break

    result = current_room.process_command(command, inventory)
    if isinstance(result, Room):
        current_room = result
        continue
    elif isinstance(result, str):
        print result
        continue
    else:
        print "I don't know what you mean"