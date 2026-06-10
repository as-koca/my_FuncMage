#!/usr/bin/env python3

# why max and min needs to be keyed??
# is constructing lists on filter and map ok?

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_list: list[dict] = sorted(
        artifacts, key=lambda a: a['power'], reverse=True)
    return sorted_list


# mypy complain: returning filter object instead of list, added list construct
def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    new_list = list(filter(lambda m: m['power'] >= min_power, mages))
    return new_list


# same as above
def spell_transformer(spells: list[str]) -> list[str]:
    new_list = list(map(lambda s: ''.join(f"* {s} *"), spells))
    return new_list


def mage_stats(mages: list[dict]) -> dict:
    stats: dict = {}
    stats['max_power'] = max(mages, key=lambda d: d['power'])['power']
    stats['min_power'] = min(mages, key=lambda d: d['power'])['power']
    stats['avg_power'] = round(
        sum(value['power'] for value in mages) / len(mages), 2)
    return stats


def test() -> None:
    artifacts = [{'name': 'Shadow Blade', 'power': 109, 'type': 'weapon'},
                 {'name': 'Ice Wand', 'power': 92, 'type': 'weapon'},
                 {'name': 'Shadow Blade', 'power': 105, 'type': 'armor'},
                 {'name': 'Light Prism', 'power': 115, 'type': 'accessory'}]
    mages = [{'name': 'Storm', 'power': 50, 'element': 'ice'},
             {'name': 'Riley', 'power': 92, 'element': 'fire'},
             {'name': 'Riley', 'power': 57, 'element': 'light'},
             {'name': 'Storm', 'power': 66, 'element': 'earth'},
             {'name': 'Phoenix', 'power': 89, 'element': 'fire'}]
    spells = ['darkness', 'heal', 'lightning', 'tornado']

    print("Testing artifact sorter...")
    sorted_artifs = artifact_sorter(artifacts)
    i = 0
    for item in sorted_artifs:
        print(f"{i}: {item['name']} ({item['power']} power)")
        i += 1

    print("\nTesting spell transformer...")
    new_spells: list[str] = spell_transformer(spells)
    for spell in new_spells:
        print(spell, end=' ')

    print("\n\nTesting power filter...")
    filtered_mages: list[dict] = power_filter(mages, 60)
    for mage in filtered_mages:
        print(f"Min power: 60 - Mage's power: {mage['power']}")

    print("\nTesting mage stats...")
    stats: dict = mage_stats(mages)
    print(f"Max power (should be 92): {stats['max_power']}")
    print(f"Min power (should be 50): {stats['min_power']}")
    print(f"Avg power (should be 70,8): {stats['avg_power']}")


if __name__ == "__main__":
    test()

#
# def n() -> None:
#     mages = [{'name': 'Storm', 'power': 50, 'element': 'ice'},
#              {'name': 'Riley', 'power': 92, 'element': 'fire'},
#              {'name': 'Riley', 'power': 57, 'element': 'light'},
#              {'name': 'Storm', 'power': 66, 'element': 'earth'},
#              {'name': 'Phoenix', 'power': 89, 'element': 'fire'}]
#     i = max(mages, key=lambda d: d['power'])
#     print(i)
#     stats = round(
#         sum(value['power'] for value in mages) / len(mages), 2)
#     print(stats)
#
