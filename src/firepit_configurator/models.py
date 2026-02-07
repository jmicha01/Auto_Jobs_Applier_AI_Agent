from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable, Sequence


class FuelType(str, Enum):
    GAS = "gas"
    PROPANE = "propane"
    WOOD = "wood"


class BaseSize(str, Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class BurnerType(str, Enum):
    STANDARD = "standard"
    HIGH_OUTPUT = "high_output"


class FinishType(str, Enum):
    STEEL = "steel"
    STAINLESS = "stainless"
    COPPER = "copper"
    CONCRETE = "concrete"


@dataclass(frozen=True)
class BaseOption:
    name: str
    size: BaseSize
    base_price: float
    compatible_fuels: tuple[FuelType, ...]

    def supports_fuel(self, fuel: FuelType) -> bool:
        return fuel in self.compatible_fuels


@dataclass(frozen=True)
class BurnerOption:
    name: str
    burner_type: BurnerType
    btus: int
    price: float
    compatible_fuels: tuple[FuelType, ...]

    def supports_fuel(self, fuel: FuelType) -> bool:
        return fuel in self.compatible_fuels


@dataclass(frozen=True)
class FinishOption:
    name: str
    finish_type: FinishType
    price: float
    compatible_sizes: tuple[BaseSize, ...]

    def supports_size(self, size: BaseSize) -> bool:
        return size in self.compatible_sizes


@dataclass(frozen=True)
class AccessoryOption:
    name: str
    price: float
    requires_fuel: tuple[FuelType, ...] | None = None

    def supports_fuel(self, fuel: FuelType) -> bool:
        if self.requires_fuel is None:
            return True
        return fuel in self.requires_fuel


@dataclass(frozen=True)
class FirepitConfiguration:
    fuel_type: FuelType
    base: BaseOption
    burner: BurnerOption
    finish: FinishOption
    accessories: tuple[AccessoryOption, ...] = field(default_factory=tuple)

    def total_price(self) -> float:
        accessory_total = sum(accessory.price for accessory in self.accessories)
        return self.base.base_price + self.burner.price + self.finish.price + accessory_total

    def accessory_names(self) -> list[str]:
        return [accessory.name for accessory in self.accessories]

    @staticmethod
    def _ensure_unique_names(options: Sequence[AccessoryOption]) -> None:
        seen: set[str] = set()
        for option in options:
            if option.name in seen:
                raise ValueError(f"Duplicate accessory: {option.name}")
            seen.add(option.name)

    @classmethod
    def from_selection(
        cls,
        *,
        fuel_type: FuelType,
        base: BaseOption,
        burner: BurnerOption,
        finish: FinishOption,
        accessories: Iterable[AccessoryOption] = (),
    ) -> "FirepitConfiguration":
        accessory_list = tuple(accessories)
        cls._ensure_unique_names(accessory_list)
        return cls(
            fuel_type=fuel_type,
            base=base,
            burner=burner,
            finish=finish,
            accessories=accessory_list,
        )
