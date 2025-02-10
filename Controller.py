from View import App
from SimplifyFunction import SimplifyFraction

#TODO handle bad input

class SimplifyFunctionApp:
    def __init__(self):
        self.view = App(self)
    
    def simplify(self, numerator, denominator):
        return SimplifyFraction(int(numerator), int(denominator)).get_simplified_fraction()
    
    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    app = SimplifyFunctionApp()
    app.run()