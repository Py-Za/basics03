class Tiger:
    __tiger_counter = 0

    def __init__(self, name):
        self.name = name
        self.__handle_birth()
        Tiger.__tiger_counter += 1

    @staticmethod
    def __handle_birth():
        print("aaAaAAaaaA KURWAAa")

    @classmethod
    def get_tiger_count(cls):
        return cls.__tiger_counter


tiger = Tiger("chujek")
print(Tiger.get_tiger_count())
print(tiger.name)

