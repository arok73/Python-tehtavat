class Robot:
    def action(self):
        print('Robot action')


class HelloRobot(Robot):
    def action(self):
        print('Hello world')


class DummyRobot(Robot):
    def start(self):
        print('Started.')


r = HelloRobot()
d = DummyRobot()

r.action()
d.action()
