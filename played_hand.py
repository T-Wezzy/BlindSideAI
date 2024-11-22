class PlayedHand:

    def __init__(self, currentHand, currentSuits):
        self.currentHand = currentHand
        self.suits = currentSuits

    def printLogicalResponse(self):
        final_output = "This is what you should do: "
        if self.straight():
            final_output += "You should play a straight... cuz uh... you kinda have one. figure it out yourself, I can't really count yet..."
        else: 
            final_output += "Die... or just play high card, your choice >:)"

        print(final_output)

    def straight(self):
        if "A" in self.currentHand and "K" in self.currentHand and "Q" in self.currentHand and "J" in self.currentHand and "10" in self.currentHand:
            return True
        elif "K" in self.currentHand and "Q" in self.currentHand and "J" in self.currentHand and "10" in self.currentHand and "9" in self.currentHand:
            return True
        elif "Q" in self.currentHand and "J" in self.currentHand and "10" in self.currentHand and "9" in self.currentHand and "8" in self.currentHand:
            return True
        elif "J" in self.currentHand and "10" in self.currentHand and "9" in self.currentHand and "8" in self.currentHand and "7" in self.currentHand:
            return True
        elif "10" in self.currentHand and "9" in self.currentHand and "8" in self.currentHand and "7" in self.currentHand and "6" in self.currentHand:
            return True
        elif "9" in self.currentHand and "8" in self.currentHand and "7" in self.currentHand and "6" in self.currentHand and "5" in self.currentHand:
            return True
        elif "8" in self.currentHand and "7" in self.currentHand and "6" in self.currentHand and "5" in self.currentHand and "4" in self.currentHand:
            return True
        elif "7" in self.currentHand and "6" in self.currentHand and "5" in self.currentHand and "4" in self.currentHand and "3" in self.currentHand:
            return True
        elif "6" in self.currentHand and "5" in self.currentHand and "4" in self.currentHand and "3" in self.currentHand and "2" in self.currentHand:
            return True
        elif "5" in self.currentHand and "4" in self.currentHand and "3" in self.currentHand and "2" in self.currentHand and "A" in self.currentHand:
            return True
        else:
            return False
    
    # def flush(self):
