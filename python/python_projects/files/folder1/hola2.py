class Worker:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hi(self):
        return "hi my name is " + self.name


if __name__ == "__main__":
    worker1 = Worker("bob",25)
    print(worker1.say_hi())