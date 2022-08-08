class Phone:

    default_color = 'Grey'
    default_model = 'C385'

    def __init__(self, color, model):
        # Динамические поля (переменные объекта)
        self.color = color
        self.model = model

    def turn_on(self):
        print("Iphone is alvie")
        pass

    def call(self, number):
        print(f"calling {number}...")
        pass

mobilephone = Phone("Blue", "Iphone")
mobilephone.turn_on()
mobilephone.call(89270187935)