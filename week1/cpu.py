from abc import ABC, abstractmethod


class CPU(ABC):
    @abstractmethod
    def process(self, data: list) -> list:
        pass


class SingleCoreCPU(CPU):
    def process(self, data: list) -> list:
        return [data]


class DoubleCoreCPU(CPU):
    def process(self, data: list) -> list:
        return [data[::2], data[1::2]]


class CPUFactory:
    @staticmethod
    def make_cpu(type: str) -> CPU:
        if type == "single":
            return SingleCoreCPU()
        elif type == "dual":
            return DoubleCoreCPU()
        else:
            raise ValueError(f"Invalid CPU type: {type}")
