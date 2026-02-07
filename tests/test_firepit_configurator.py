import pytest

from src.firepit_configurator import (
    BaseOption,
    BaseSize,
    BurnerOption,
    BurnerType,
    FinishOption,
    FinishType,
    FirepitCatalog,
    FirepitConfigurator,
    FuelType,
)


def test_configuration_total_and_validation():
    base = BaseOption(
        name="Mesa",
        size=BaseSize.SMALL,
        base_price=450.0,
        compatible_fuels=(FuelType.GAS,),
    )
    burner = BurnerOption(
        name="Ember",
        burner_type=BurnerType.STANDARD,
        btus=40000,
        price=220.0,
        compatible_fuels=(FuelType.GAS,),
    )
    finish = FinishOption(
        name="Stainless",
        finish_type=FinishType.STAINLESS,
        price=190.0,
        compatible_sizes=(BaseSize.SMALL,),
    )

    configurator = FirepitConfigurator(catalog=FirepitCatalog())
    configuration = configurator.configure(
        fuel_type=FuelType.GAS,
        base=base,
        burner=burner,
        finish=finish,
        accessories=(),
    )

    assert configuration.total_price() == pytest.approx(860.0)


def test_incompatible_finish_raises():
    base = BaseOption(
        name="Summit",
        size=BaseSize.LARGE,
        base_price=950.0,
        compatible_fuels=(FuelType.GAS,),
    )
    burner = BurnerOption(
        name="Ember",
        burner_type=BurnerType.STANDARD,
        btus=40000,
        price=220.0,
        compatible_fuels=(FuelType.GAS,),
    )
    finish = FinishOption(
        name="Copper",
        finish_type=FinishType.COPPER,
        price=260.0,
        compatible_sizes=(BaseSize.SMALL,),
    )

    configurator = FirepitConfigurator(catalog=FirepitCatalog())

    with pytest.raises(ValueError, match="does not support base size"):
        configurator.configure(
            fuel_type=FuelType.GAS,
            base=base,
            burner=burner,
            finish=finish,
        )
