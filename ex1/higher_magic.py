#!/usr/bin/env python3

from collections.abc import Callable

# returns desc of what happened

# === Exercise 1 Test Data ===
# # Higher Realm Test Data
# # Use these in your test functions:
# test_values = [17, 25, 7]
# test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def heal(target: str, power: int) -> str:
    return f"{target} healed for {power} HP."


def attack(target: str, power: int) -> str:
    return f"{target} lost {power} HP from attack!"


def freeze(target: str, power: int) -> str:
    return f"{target} frozen for {power} seconds!"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine(target: str, power: int) -> tuple:
        t: tuple[str, str] = (spell1(target, power), spell2(target, power))
        return (t)
    return combine


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplify(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplify


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def chance(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return chance


def spell_sequence(spells: list[Callable]) -> Callable:
    def seq(target: str, power: int) -> list[str]:
        spell_list: list[str] = []
        for spell in spells:
            spell_list.append(spell(target, power))
        return spell_list
    return seq


def test() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(attack, heal)
    t = combined('Dragon', 17)
    print(f"Combined spell result: {t[0]}, {t[1]}")

    print("\nTesting power amplifier...")
    amplify = power_amplifier(attack, 3)
    s = amplify('Knight', 10)
    print(f"Original: {attack('Knight', 10)}, Amplified: {s}")

    print("\nTesting conditional caster...")
    ct = conditional_caster(lambda target, power: power > 10, heal)
    print(f"Condition True: {ct('Mage', 24)}")
    print(f"Condition False: {ct('Mage', 4)}")

    print("\nTesting spell sequence...")
    spelist = [attack, heal, freeze]
    seq = spell_sequence(spelist)
    retlist = seq("Wizard", 10)
    for ret in retlist:
        print(ret)

    print("\nChecking that every return is Callable:")
    print(callable(combined))
    print(callable(amplify))
    print(callable(ct))
    print(callable(seq))


if __name__ == "__main__":
    test()
