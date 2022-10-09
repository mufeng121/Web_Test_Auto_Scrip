from . import attack as a

class SQL_injector(a.attack_inter):
    def init(self):
        print("init")

    def generator(self):
        print("generate")

    def run(self):
        print("run")