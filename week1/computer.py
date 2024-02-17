from cpu import CPU, CPUFactory
from memory import RAM, ROM, RamFactory, RomFactory


class Computer:
    cpu: CPU
    ram: RAM
    rom: ROM

    def bootstrap(self) -> dict:
        return {
            "cpu_processed": self.cpu.process(self.rom.data),
            "ram_data": self.ram.data,
            "rom_data": self.rom.data,
        }


class ComputerBuilder:
    @staticmethod
    def produce_cpu(c: Computer, type: str) -> None:
        c.cpu = CPUFactory.make_cpu(type)

    @staticmethod
    def produce_ram(c: Computer, size: int) -> None:
        c.ram = RamFactory.make_memory(size=size)

    @staticmethod
    def produce_rom(c: Computer, data: list) -> None:
        c.rom = RomFactory.make_memory(data=data)

    @classmethod
    def build_computer(cls, type: str) -> Computer:
        computer = Computer()
        if type == "laptop":
            cls.produce_cpu(computer, "single")
            cls.produce_ram(computer, 8)
            cls.produce_rom(computer, [1, 2, 3, 4])
            return computer
        elif type == "desktop":
            cls.produce_cpu(computer, "dual")
            cls.produce_ram(computer, 16)
            cls.produce_rom(computer, [1, 2, 3, 4, 5, 6, 7, 8])
            return computer
        else:
            raise ValueError("Invalid computer type")
