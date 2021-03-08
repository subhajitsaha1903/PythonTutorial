class computer:
    def __init__(self, cpu, ram):
        # return "in init"
        self.cpu = cpu
        self.ram = ram

    def config(self):
        # return "Hello OOPs"
        return "config is", self.cpu, self.ram


comp1 = computer('Intel i5', '8 GB')

# print(type(comp1))
print(comp1.config())
# print(computer.config(comp1))
# a = 2
