from Tile import Tile


class MapHandler:
    def __init__(self, file1 = 'map1.txt', file1b = 'map1b.txt'):
        self.map_a = ""
        self.map_b = ""
        self.load(file1, file1b)

    def load(self, filename, filebname):
        map_file1 = open(filename, 'r')
        map_file1b = open(filebname, 'r')
        self.map_a = self.parse_file(map_file1)
        self.map_b = self.parse_file(map_file1b)

    @staticmethod
    def parse_file(file_in):
        num_tiles = 0
        x = y = 0
        map_out = []
        for row in file_in:
            for col in row:
                if col == "P":
                    t = Tile(x, y, 1)
                    map_out.append(t)
                    num_tiles +=1
                    # entities.add(t)
                if col == "E":
                    e = Tile(x, y, 2)
                    map_out.append(e)
                    num_tiles +=1
                    # entities.add(e)
                x += 32
               # num_tiles +=1
            y += 32
            x = 0
        print "read ",num_tiles," into map"
        return map_out
