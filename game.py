import math

class Location:
    def __init__(self, name: str, width: int, height: int, length: int):
        self.name = name
        self._width = width
        self._height = height
        self._length = length

    def isInside(self, x, y, z) -> bool:
        return ((x > 0 and x < self._length)
                and (y > 0 and y < self._width)
                and (z > 0 and z < self._height))

    @property
    def width(self):
        return self._width

    @property
    def length(self) -> int:
        return self._length

    @property
    def height(self):
        return self._height

    @property
    def volume(self):
        return self.height * self.length * self.width


class GameObject:
    def __init__(self, name: str, loc: Location, x, y, z):
        self.name = name
        self._loc = loc
        self.x, self.y, self.z = x, y, z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x < 0:
            self._x = 0
        elif self._loc.length < x:
            self._x = self._loc.length
        else:
            self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if y < 0:
            self._y = 0
        elif self._loc.width < y:
            self._y = self._loc.width
        else:
            self._y = y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        if z < 0:
            self._z = 0
        elif self._loc.height < z:
            self._z = self._loc.height
        else:
            self._z = z

    def move(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def distance(self, obj: GameObject):
        dx = self.x - obj.x
        dy = self.y - obj.y
        dz = self.z - obj.z
        r2 = dx ** 2 + dy ** 2 + dz ** 2
        return int(math.sqrt(r2))

class LivingObject(GameObject):
    def __init__(self, name: str, loc: Location, x, y, z, hp: int):
        super().__init__(name, loc, x, y, z)
        self._max_hp = hp
        self._hp = hp

    @property
    def maxHP(self):
        return self._max_hp

    @property
    def hp(self):
        return self._hp

    def changeHP(self, change):
        if not self.alive:
            return
        self._hp += change
        if self._hp < 0:
            self._hp = 0
        if self._hp > self._max_hp:
            self._hp = self._max_hp

    @property
    def alive(self):
        return self._hp > 0

class Weapon(GameObject):
    def __init__(self, name: str, loc: Location, x, y, z, damage, radius):
        super().__init__(name, loc, x, y, z)
        self._damage = damage
        self._radius = radius

    @property
    def damage(self):
        return self._damage

    @property
    def radius(self):
        return self._radius

    def attack(self, obj: LivingObject):
        d = self.distance(obj)
        if d > self.radius:
            return
        obj.changeHP(-self.damage)
