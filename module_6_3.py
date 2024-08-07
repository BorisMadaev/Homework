class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance = self.y_distance + dy


class Horse(Eagle):
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.x_distance = self.x_distance + dx

    def voice(self):
        return super().sound


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        kort = (self.x_distance, self.y_distance)
        return kort

    def voice(self):
        self.sound = super().voice()
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
