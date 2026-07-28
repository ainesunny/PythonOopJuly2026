class Range:
    def __init__(self, start: float, end: float) -> None:
        self.__start = start
        self.__end = end

    @property
    def start(self) -> float:
        return self.__start

    @start.setter
    def start(self, start: float) -> None:
        self.__start = start

    @property
    def end(self) -> float:
        return self.__end

    @end.setter
    def end(self, end: float) -> None:
        self.__end = end

    @property
    def length(self) -> float:
        return self.__end - self.__start

    def is_inside(self, number: float) -> bool:
        return self.__start <= number <= self.__end

    def get_intersection(self, other: Range) -> Range | None:
        intersection_start = max(self.__start, other.__start)
        intersection_end = min(self.__end, other.__end)
        return Range(intersection_start, intersection_end) if intersection_start < intersection_end else None

    def get_union(self, other: Range) -> list[Range]:
        if self.__start <= other.__start:
            left_range, right_range = self, other
        else:
            left_range, right_range = other, self

        if left_range.__end >= right_range.__start:
            return [Range(left_range.__start, max(left_range.__end, right_range.__end))]
        else:
            return [Range(left_range.__start, left_range.__end), Range(right_range.__start, right_range.__end)]

    def get_difference(self, other: Range) -> list[Range]:
        difference_ranges = []

        if self.__start < other.__start:
            difference_ranges.append(Range(self.__start, min(self.__end, other.__start)))

        if self.__end > other.__end:
            difference_ranges.append(Range(max(self.__start, other.__end), self.__end))

        return difference_ranges

    def __repr__(self) -> str:
        return f"({self.__start!r}, {self.__end!r})"
