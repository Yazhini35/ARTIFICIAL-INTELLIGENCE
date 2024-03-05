class VacuumCleaner:
    def __init__(self):
        self.position = 0
        self.dirt_positions = [2, 4, 7] 
    
    def move(self, position):
        self.position = position
        print("Moving to position", self.position)
    
    def clean(self, position):
        if position in self.dirt_positions:
            self.dirt_positions.remove(position)
            print("Cleaning dirt at position", position)
        
    def check_dirt(self):
        print("Dirt positions:", self.dirt_positions)
    
    def clean_all_dirt(self):
        while self.dirt_positions:
            current_position = self.dirt_positions[0]
            self.move(current_position)
            self.clean(current_position)
            self.check_dirt()
        print("No more dirt to clean.")
    
vacuum = VacuumCleaner()
vacuum.clean_all_dirt()
