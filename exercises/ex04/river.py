"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear

class River:
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        alive_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                alive_fish.append(fish)
        self.fish = alive_fish

        alive_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                alive_bears.append(bear)
        self.bears = alive_bears

    def bears_eating(self) -> None:
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
    
    def check_hunger(self) -> None:
        alive_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)
        self.bears = alive_bears
        
    def repopulate_fish(self) -> None:
        newer_fish = (len(self.fish) // 2) * 4
        for i in range(newer_fish):
            self.fish.append(Fish())
    
    def repopulate_bears(self) -> None:
        newer_bears = len(self.bears) // 2
        for i in range(newer_bears):
            self.bears.append(Bear())
    
    def view_river(self) -> None:
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        for i in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        for i in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)