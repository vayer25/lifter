
class Hand:
    def __init__(self):
        self.name = "Hand"

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Leg:
    def __init__(self):
        self.name = "Leg"

class Foot:
    def __init__(self):
        self.name = "Foot"

class Head:
    def __init__(self):
        self.name = "Head"

class Chest:
    def __init__(self):
        self.name = "Chest"

class Stomach:
    def __init__(self):
        self.name = "Stomach"


class Torso:
    def __init__(self, head, right_arm, chest, left_arm, stomach,
                 right_leg, left_leg, right_foot, left_foot):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.chest = chest
        self.stomach = stomach
        self.right_leg = right_leg
        self.left_leg = left_leg
        self.right_foot = right_foot
        self.left_foot = left_foot


    def describe(self):
        print("Body parts in the torso:")
        print("This is the part of the body: Head:", self.head.name)
        print("This is the part of the body: Right Arm with", self.right_arm.hand.name)
        print("This is the part of the body: Left Arm with", self.left_arm.hand.name)
        print("This is the part of the body: Chest:", self.chest.name)
        print("This is the part of the body: Stomach:", self.stomach.name)
        print("This is the part of the body: Right Leg:", self.right_leg.name)
        print("This is the part of the body: Left Leg:", self.left_leg.name)
        print("This is the part of the body: Right Foot:", self.right_foot.name)
        print("This is the part of the body: Left Foot:", self.left_foot.name)



right_hand = Hand()
left_hand = Hand()

right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

right_leg = Leg()
left_leg = Leg()

right_foot = Foot()
left_foot = Foot()

head = Head()
chest = Chest()
stomach = Stomach()


torso = Torso(
    head,
    right_arm,
    chest,
    left_arm,
    stomach,
    right_leg,
    left_leg,
    right_foot,
    left_foot
)

torso.describe()