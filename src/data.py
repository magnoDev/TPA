class Data:

    def __init__(self, email, gender, uid, birthdate, height, weight):
        self.email = email
        self.gender = gender
        self.uid = uid
        self.birthdate = birthdate
        self.height = height
        self.weight = weight

    def bigger_than(self, other):
        return self.uid > other.uid

    def smaller_than(self, other):
        return self.uid < other.uid
