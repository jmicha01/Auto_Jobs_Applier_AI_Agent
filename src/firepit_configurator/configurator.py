from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from .models import (
    AccessoryOption,
    BaseOption,
    BurnerOption,
    FinishOption,
    FirepitConfiguration,
    FuelType,
)


@dataclass
class FirepitCatalog:
    bases: list[BaseOption] = field(default_factory=list)
    burners: list[BurnerOption] = field(default_factory=list)
    finishes: list[FinishOption] = field(default_factory=list)
    accessories: list[AccessoryOption] = field(default_factory=list)

    def add_base(self, base: BaseOption) -> None:
        self.bases.append(base)

    def add_burner(self, burner: BurnerOption) -> None:
        self.burners.append(burner)

    def add_finish(self, finish: FinishOption) -> None:
        self.finishes.append(finish)

    def add_accessory(self, accessory: AccessoryOption) -> None:
        self.accessories.append(accessory)


class FirepitConfigurator:
    def __init__(self, catalog: FirepitCatalog) -> None:
        self.catalog = catalog

    def validate_configuration(self, configuration: FirepitConfiguration) -> None:
        if not configuration.base.supports_fuel(configuration.fuel_type):
            raise ValueError(
                f"Base '{configuration.base.name}' does not support fuel {configuration.fuel_type}."
            )
        if not configuration.burner.supports_fuel(configuration.fuel_type):
            raise ValueError(
                f"Burner '{configuration.burner.name}' does not support fuel {configuration.fuel_type}."
            )
        if not configuration.finish.supports_size(configuration.base.size):
            raise ValueError(
                f"Finish '{configuration.finish.name}' does not support base size {configuration.base.size}."
            )
        for accessory in configuration.accessories:
            if not accessory.supports_fuel(configuration.fuel_type):
                raise ValueError(
                    f"Accessory '{accessory.name}' does not support fuel {configuration.fuel_type}."
                )

    def configure(
        self,
        *,
        fuel_type: FuelType,
        base: BaseOption,
        burner: BurnerOption,
        finish: FinishOption,
        accessories: Iterable[AccessoryOption] = (),
    ) -> FirepitConfiguration:
        configuration = FirepitConfiguration.from_selection(
            fuel_type=fuel_type,
            base=base,
            burner=burner,
            finish=finish,
            accessories=accessories,
        )
        self.validate_configuration(configuration)
        return configuration
