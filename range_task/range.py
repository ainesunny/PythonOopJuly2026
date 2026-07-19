class Range:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end

    def get_length(self):
        return self.__end - self.__start

    def is_inside(self, number):
        return self.__start <= number <= self.__end
