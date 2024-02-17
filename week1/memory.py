from abc import ABC, abstractmethod


class Memory(ABC):
    size: int
    data: list

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def read(self, address: int) -> int:
        pass

    @abstractmethod
    def write(self, address: int, value: int):
        pass


class RAM(Memory):
    def __init__(self, size: int):
        self.size = size
        self.data = [0] * size

    def read(self, address: int) -> int:
        return self.data[address]

    def write(self, address: int, value: int):
        self.data[address] = value


class ROM(Memory):
    def __init__(self, data: list):
        self.size = len(data)
        self.data = data

    def read(self, address: int) -> int:
        return self.data[address]

    def write(self, address: int, value: int):
        raise ValueError("Cannot write to ROM")


class MemoryFactory(ABC):
    @abstractmethod
    def make_memory(self):
        pass


# 음.. 이렇게 하는거 아닌거 같은데..
class RamFactory(MemoryFactory):
    @staticmethod
    def make_memory(**kwargs) -> RAM:
        size = kwargs.get("size")
        if size is None:
            raise ValueError("Size is required for RAM")
        return RAM(size)


class RomFactory(MemoryFactory):
    @staticmethod
    def make_memory(**kwargs) -> ROM:
        data = kwargs.get("data")
        if data is None:
            raise ValueError("Data is required for ROM")
        return ROM(data)
