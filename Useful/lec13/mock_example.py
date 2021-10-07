def fun(service):
    service.run()
    print('rrr')
    service.say()



class MockService:
    name = 'Mock name'
    flag1 = False
    flag2 = False

    def run(self):
        self.flag1 = True

    def say(self):
        self.flag2 = True

s = MockService()

flag3 = False
def print(arg):
    global flag3
    flag3 = True
    assert(arg == s.name)


fun(s)
assert(s.flag1)
assert(s.flag2)
assert(flag3)
