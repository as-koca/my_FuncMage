#!/usr/bin/env python3

from collections.abc import Callable
from typing import Any
import functools as ft
import operator as op


def attack(power: int, element: str, target: str) -> str:
    return f"{target} attacked with {element} by power {power}"


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return ft.reduce(op.add, spells)
    elif operation == "multiply":
        return ft.reduce(op.mul, spells)
    elif operation == "max":
        return ft.reduce(lambda x, y: x if op.gt(x, y) else y, spells)
    elif operation == "min":
        return ft.reduce(lambda x, y: x if op.lt(x, y) else y, spells)
    raise ValueError("Error - only supported: add, multiply, max, min")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    enchantments: dict = {}
    ench1 = ft.partial(base_enchantment, 50, "Fire")
    ench2 = ft.partial(base_enchantment, 50, "Water")
    ench3 = ft.partial(base_enchantment, 50, "Air")
    enchantments['fire'] = ench1
    enchantments['water'] = ench2
    enchantments['air'] = ench3
    return enchantments


@ft.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        print("Value can't be negative")
        return 0
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @ft.singledispatch
    def dispatcher(smth: object) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(damage: int) -> str:
        return f"{damage} damage"

    @dispatcher.register
    def _(enchantment: str) -> str:
        return f"{enchantment} enchantment"

    @dispatcher.register
    def _(spells: list) -> str:
        return f"{len(spells)} spells"
    return dispatcher


if __name__ == "__main__":
    spells = [19, 29, 29, 18, 38, 42]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [8, 14, 8]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, "add")}")
    print(f"Product: {spell_reducer(spells, "multiply")}")
    print(f"Smallest: {spell_reducer(spells, "min")}")
    print("Invalid option:", end=' ')
    try:
        spell_reducer(spells, "not valid")
    except ValueError as e:
        print(e)

    print("\nTesting partial enchantment...")
    enchantments = partial_enchanter(attack)
    print(f"Enchantment 1: {enchantments['fire']("Wizard")}")
    print(f"Enchantment 2: {enchantments['water']('Giant')}")
    print(f"Enchantment 3: {enchantments['air']('Knight')}")

    print("\nTesting memoized fibonacci...")
    print(memoized_fibonacci(10))
    # will show 'hits=8', means it re-used valued cached 8 times
    # and didn't need to recompute the function
    print(memoized_fibonacci.cache_info())
