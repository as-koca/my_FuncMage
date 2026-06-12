#!/usr/bin/env python3

from typing import Any
from collections.abc import Callable
from time import time, sleep
import functools as ft


def spell_timer(func: Callable) -> Callable:

    @ft.wraps(func)
    def timer(*args, **kwargs) -> Any:
        print(f"Casting {timer.__name__}")
        start = time()
        res = func(*args, **kwargs)
        end = time()
        elapsed = end - start
        print(f"Spell completed in {round(elapsed, 3)} seconds")
        return res
    return timer


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @ft.wraps(func)
        def validator(*args, **kwargs) -> str:
            power = args[-1]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return validator
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @ft.wraps(func)
        def retry(*args, **kwargs) -> str:
            for attempt in range(1, max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying...", end=' ')
                    print(f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return retry
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        digits = range(9)
        if len(name) < 3:
            return False
        for dig in digits:
            if str(dig) in name:
                return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Succesfully cast {spell_name} with {power}"


if __name__ == "__main__":
    # --- TEST FUNCTIONS --- #
    @spell_timer
    def fireball(power: int, target: str) -> str:
        sleep(0.10123)
        return f"{target} hit by fireball, lost {power} HP"

    @power_validator(20)
    def earthquake(power) -> str:
        return f"Earthquake power: {power}"

    @retry_spell(3)
    def freeze(power: int) -> str:
        if power < 100:
            power += 30
        if power < 100:
            raise ValueError("Power must be at least 100.")
        return "Attack with freeze succesful!"
    # --- TEST FUNCTIONS --- #

    print("Testing spell timer...")
    print(f"Result: {fireball(50, "Mage")}")

    print("\nTesting power validator...")
    print(f"Test 0, valid: {earthquake(50)}")
    print(f"Test 0, invalid: {earthquake(10)}")

    print("\nTesting retry spell...")
    print(f"{freeze(20)}\n")
    print(freeze(80))

    print("\nTesting MageGuild...")
    mg = MageGuild()
    print(f"Name Nora: {mg.validate_mage_name("Nora")}")
    print(f"Name a23aaa: {mg.validate_mage_name("a23aaa")}")
    print(f"Name Z: {mg.validate_mage_name("Z")}")
    print(mg.cast_spell("wet napkin", 1000000))
    print(mg.cast_spell("Deadly Whirlwind", 2))
