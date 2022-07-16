
class A:
    def init(self):
        self.mas = []

    def append_element(self, element):
        self.mas.append(element)
        

    def get_element(self):
        out = self.mas.pop(0) if self.mas else None
        #out = self.mas[0]
        #del self.mas[0]
        #print(out)
        return out

    def print_list(self):
        print(self.mas)
        
        
a = A()
a.append_element(5)
a.append_element("a")
a.append_element("r")
a.print_list()
print(a.get_element())
print(a.get_element())
a.print_list()