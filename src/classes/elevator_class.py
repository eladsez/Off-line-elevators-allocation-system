'''this class holds an elevator object'''

class Elevator(object):
    def __init__(self, id: int = None, speed: float = None, min_floor: int = None, max_floor: int = None,
                 close_time: float = None, open_time: float = None, start_time: float = None, stop_time: float = None):
        '''

        :param id: elevator index.
        :param speed: how many floors a second this elevator pass.
        :param min_floor: min floor this elevator can reach.
        :param max_floor: max floor this elevator can reach.
        :param close_time: how much time it takes the elevator to close it's doors.
        :param open_time: how much time it takes the elevator to open it's doors.
        :param start_time: how much time it takes the elevator to start moving at full speed.
        :param stop_time: how much time it takes the elevator to stop moving.
        '''
        self.id = id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time

    def __str__(self):
        return f"id: {self.id}, speed: {self.speed}, min floor: {self.min_floor}, max floor: {self.max_floor}, close " \
               f"time: {self.close_time}, open time: {self.open_time}, start time: {self.start_time}, stop" \
               f" time: {self.stop_time} "

    '''this function initialize an elevator object from a list extracted from a building json file'''
    def init_from_list(elev_list: list = None):
        new_list = []
        for i in elev_list:
            curr_elev = Elevator(id=i["_id"], speed=i["_speed"], min_floor=i["_minFloor"],
                                 max_floor=i["_maxFloor"], close_time=i["_closeTime"],
                                 open_time=i["_openTime"], start_time=i["_startTime"],
                                 stop_time=i["_stopTime"])
            new_list.append(curr_elev)
        return new_list

    def __lt__(self, other):
        return self.speed < other.speed

    def __repr__(self):
        return self.__str__()

# if __name__ == '__main__':
#     e = Elevator(2, 2.0, 0, 10, 0.2, 0.3, 0.1, 0.4)
#     e1 = Elevator(8, 5.2, 0, 10, 0.2, 0.3, 0.1, 0.4)
#     e2 = Elevator(6, 8.5, 0, 10, 0.2, 0.3, 0.1, 0.4)
#     l = [e,e1,e2]
#     print(l)
#     print("\n")
#     l.sort()
#     print(l)
