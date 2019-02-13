class my_list(list):
    def get(self, i):
        try:
            return self[i]
        except IndexError:
            return False

a = my_list()

print(a.get(4))