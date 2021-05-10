class Garden:
    def __init__(self, plants=[]):
        self.plants = []
        for plant in plants:
            self.add_plant(plant)

    def add_plant(self, plant_object):
        if not self.has_plant(plant_object):
            self.plants.append(plant_object)

    def has_plant(self, plant_object):
        found = False
        for plant in self.plants:
            if plant.name == plant_object.name:
                found = True
        return found

    def set_plants_next_to_object(self):
        for plant_main in self.plants:
            for plant_secondary in self.plants:
                plant_main.try_add_plant(plant_secondary)

    def __str__(self):
        out = ""
        for plant in self.plants:
            out += plant.name + "\t| "
            for plant_next_to in plant.plants_next_to_object:
                out += plant_next_to.name + " "
            out += "\n"
        return out
