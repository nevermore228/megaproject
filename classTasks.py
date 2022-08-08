import time


class Phone:

    default_color = 'Grey'
    default_model = 'C385'
    turn_on = False

    def __init__(self, color, model):
        # Динамические поля (переменные объекта)
        self.color = color
        self.model = model

    def call(self, number):
        print(f"calling {number}...")
        pass
    def turn_on_phone(self):
        if self.turn_on == False:
            self.turn_on = True
            print("Hello!")
        else:
            print("Phone is awake!")


mobilephone = Phone("Blue", "Iphone")
mobilephone.turn_on_phone()
mobilephone.call(89270187935)

print(dir(mobilephone))
