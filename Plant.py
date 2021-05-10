from Garden import Garden


class Plant(Garden):
    def __init__(self, name, plants_next_to=[]):
        self.name = name
        self.plants_next_to_names = plants_next_to
        self.plants_next_to_object = []

    def try_add_plant(self, other_plant):
        for plantName in self.plants_next_to_names:
            if plantName == other_plant.name:
                self.plants_next_to_object.append(other_plant)
