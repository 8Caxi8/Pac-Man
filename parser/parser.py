import sys
import json
import re

DEFAULTS = {
    "highscore_filename": "highscores.json",
    "lives": 3,
    "pacgum": 42,
    "points_per_pacgum": 10,
    "points_per_super_pacgum": 50,
    "points_per_ghost": 200,
    "seed": 42,
    "level_max_time": 90,
    "levels": list(range(1, 11))
}


class ParserError(Exception):
    pass


def parser() -> dict[str, object]:
    arg = sys.argv[1:]

    if len(arg) != 1:
        raise ParserError("Only one argument allowed: The configuration file")

    path = arg[0]
    try:
        with open(path) as f:
            content = f.read()
            raw = re.sub(r'^\s*#.*$', '', content, flags=re.MULTILINE)
            raw = re.sub(r'^\s*//.*$', '', raw, flags=re.MULTILINE)
            raw = re.sub(r'/\*.*?\*/', '', raw, flags=re.DOTALL)
        data = json.loads(raw)
    except FileNotFoundError:
        raise ParserError(f"Config file not found: {path}")

    except json.JSONDecodeError as e:
        raise ParserError(f"Invalid JSON in config: {e}")

    config = DEFAULTS.copy()
    for key, default in DEFAULTS.items():
        if key not in data:
            print(f"Missing key '{key}', using default: {default}")
            config[key] = default
            continue

        val = data.get(key, default)
        if not isinstance(val, type(default)) or (key == "levels" and not val):
            print(f"Invalid value for '{key}', using default: {default}")
            config[key] = default

        else:
            config[key] = val

    return config
