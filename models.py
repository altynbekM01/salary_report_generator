from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    department: str
    hours_worked: float
    hourly_rate: float

    def payout(self) -> float:
        return self.hours_worked * self.hourly_rate
