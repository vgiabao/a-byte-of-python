class Robot:
    ''' Represents a robot, with a name'''
    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        '''Initialise the data'''
        self.name = name
        print('initialise {0}'.format(self.name))
        Robot.population += 1
    def die(self):
        print('{} is detroyed'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{} is the last one'.format(self.name))
        else:
            print('There are still {} Robots working'.format(Robot.population))
    def say_hi(self):
        print('Greeting, Master call me {}'.format(self.name))
    @classmethod
    def how_many(cls):
        print('we have {:d} Robot'.format(Robot.population))

droid1= Robot('R2-D2')
droid2= Robot('R3-D3')
Robot.how_many()
droid1.say_hi()
print('Robots are doing somethings')
print('Work done! Destroying them')
droid1.die()
droid2.die()
Robot.how_many()