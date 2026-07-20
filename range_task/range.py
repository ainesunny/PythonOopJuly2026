class Range:
    def __init__(self, start: int, end: int) -> None:
        self.__start = start
        self.__end = end

    @property
    def start(self) -> int:
        return self.__start

    @start.setter
    def start(self, start: int) -> None:
        self.__start = start

    @property
    def end(self) -> int:
        return self.__end

    @end.setter
    def end(self, end: int) -> None:
        self.__end = end

    def get_length(self) -> int:
        return self.__end - self.__start

    def is_inside(self, number: int) -> bool:
        return self.__start <= number <= self.__end

    def intersection(self, second_range: Range) -> Range | None:
        intersection_start = max(self.__start, second_range.start)
        intersection_end = min(self.__end, second_range.end)
        return Range(intersection_start, intersection_end) if intersection_start < intersection_end else None

    def union(self, second_range: Range) -> list[Range]:
        if self.__start <= second_range.start:
            left_range, right_range = self, second_range
        else:
            left_range, right_range = second_range, self

        if left_range.__end >= right_range.start:
            return [Range(left_range.__start, max(left_range.__end, right_range.__end))]
        else:
            return [Range(left_range.__start, left_range.__end), Range(right_range.start, right_range.__end)]

    def __str__(self) -> str:
        return f"[{self.__start}, {self.__end}]"
