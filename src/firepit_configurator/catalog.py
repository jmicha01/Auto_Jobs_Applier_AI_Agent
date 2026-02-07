from __future__ import annotations

from .configurator import FirepitCatalog
from .models import (
    AccessoryOption,
    BaseOption,
    BaseSize,
    BurnerOption,
    BurnerType,
    FinishOption,
    FinishType,
    FuelType,
)


def build_default_catalog() -> FirepitCatalog:
    catalog = FirepitCatalog()

    catalog.add_base(
        BaseOption(
            name="Mesa",
            size=BaseSize.SMALL,
            base_price=450.0,
            compatible_fuels=(FuelType.GAS, FuelType.PROPANE),
        )
    )
    catalog.add_base(
        BaseOption(
            name="Ridge",
            size=BaseSize.MEDIUM,
            base_price=675.0,
            compatible_fuels=(FuelType.GAS, FuelType.PROPANE, FuelType.WOOD),
        )
    )
    catalog.add_base(
        BaseOption(
            name="Summit",
            size=BaseSize.LARGE,
            base_price=950.0,
            compatible_fuels=(FuelType.GAS, FuelType.PROPANE),
        )
    )

    catalog.add_burner(
        BurnerOption(
            name="Ember",
            burner_type=BurnerType.STANDARD,
            btus=40000,
            price=220.0,
            compatible_fuels=(FuelType.GAS, FuelType.PROPANE),
        )
    )
    catalog.add_burner(
        BurnerOption(
            name="Blaze",
            burner_type=BurnerType.HIGH_OUTPUT,
            btus=60000,
            price=360.0,
            compatible_fuels=(FuelType.GAS, FuelType.PROPANE),
        )
    )
    catalog.add_burner(
        BurnerOption(
            name="Hearth",
            burner_type=BurnerType.STANDARD,
            btus=30000,
            price=180.0,
            compatible_fuels=(FuelType.WOOD,),
        )
    )

    catalog.add_finish(
        FinishOption(
            name="Raw Steel",
            finish_type=FinishType.STEEL,
            price=0.0,
            compatible_sizes=(BaseSize.SMALL, BaseSize.MEDIUM, BaseSize.LARGE),
        )
    )
    catalog.add_finish(
        FinishOption(
            name="Stainless",
            finish_type=FinishType.STAINLESS,
            price=190.0,
            compatible_sizes=(BaseSize.SMALL, BaseSize.MEDIUM, BaseSize.LARGE),
        )
    )
    catalog.add_finish(
        FinishOption(
            name="Copper",
            finish_type=FinishType.COPPER,
            price=260.0,
            compatible_sizes=(BaseSize.SMALL, BaseSize.MEDIUM),
        )
    )
    catalog.add_finish(
        FinishOption(
            name="Concrete",
            finish_type=FinishType.CONCRETE,
            price=320.0,
            compatible_sizes=(BaseSize.MEDIUM, BaseSize.LARGE),
        )
    )

    catalog.add_accessory(
        AccessoryOption(name="Wind Guard", price=85.0)
    )
    catalog.add_accessory(
        AccessoryOption(
            name="Propane Cover",
            price=60.0,
            requires_fuel=(FuelType.PROPANE,),
        )
    )
    catalog.add_accessory(
        AccessoryOption(
            name="Log Grate",
            price=95.0,
            requires_fuel=(FuelType.WOOD,),
        )
    )

    return catalog
