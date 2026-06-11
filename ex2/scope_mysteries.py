#!/usr/bin/env python3

from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count: int = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count
    return increment


def spell_accumulator(initial_power: int) -> Callable:
    def accumulate(power: int = 0) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power
    return accumulate


# don't need nonlocal here since we ain't reassigning anclosing scope variable
def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    vault: dict = {}

    def store(key: Any, val: Any) -> None:
        vault[key] = val

    def recall(key: Any) -> Any:
        try:
            return_key = vault[key]
        except KeyError:
            return "Memory not found"
        return return_key

    action: dict = {}
    action["store"] = store
    action["recall"] = recall
    return action


# enchantment_types = ['Shocking', 'Frozen', 'Earthen']
# items_to_enchant = ['Armor', 'Cloak', 'Sword', 'Staff']
if __name__ == "__main__":
    print("Testing mage_counter...")
    c = mage_counter()
    d = mage_counter()
    a = c()
    print(f"counter_a call 1: {a}")
    a = c()
    print(f"counter_a call 2: {a}")
    b = d()
    print(f"counter_b call 1: {b}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    accumulation = accumulator()
    print(f"Initial power: {accumulation}")
    accumulation = accumulator(20)
    print(f"Base 100, add 20: {accumulation}")
    accumulation = accumulator(30)
    print(f"Base 100, add 30: {accumulation}")

    print("\nTesting enchantment factory...")
    fact1 = enchantment_factory("Flaming")
    print(f"fact1: {fact1('Sword')}")
    print(f"fact1: {fact1('Stick')}")
    fact2 = enchantment_factory("Frozen")
    print(f"fact2: {fact2('Shield')}")
    print(f"fact2: {fact2('Wind')}")

    print("\nTesting memory vault...")
    vault = memory_vault()
    storing = vault["store"]
    recall = vault["recall"]
    storing("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {recall("secret")}")
    print(f"Recall 'doenstexist': {vault["recall"]("doesntexist")}")
