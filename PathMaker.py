class PathMaker:
    def __init__(self, plant, distance, path = []):
        self.current_plant = plant
        self.can_be_next_to = []
        self.distance = distance
        self.pos_on = 0
        self.path = path + [plant.name]

    def is_end(self):
        return self.pos_on == len(self.current_plant.plants_next_to_object)

    def make_list(self):
        out = []
        for plant_possible in self.current_plant.plants_next_to_object:
            out.append(PathMaker(plant_possible, self.distance-1))
        return out

    def get_path(self, distance):
        # print(array)
        if distance != 1:
            listI = self.current_plant.plants_next_to_object[self.pos_on]
            self.pos_on+=1
            next_Path = PathMaker(listI, self.distance-1, self.path)
            return next_Path.get_path(distance - 1)
        return self.path

