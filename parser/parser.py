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
    "levels": []
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
            raw = re.sub(r'^\s*#.*$', '', f.read(), flags=re.MULTILINE)
        data = json.loads(raw)
    except FileNotFoundError:
        raise ParserError(f"Config file not found: {path}")

    except json.JSONDecodeError as e:
        raise ParserError(f"Invalid JSON in config: {e}")

    config = DEFAULTS.copy()
    for key, default in DEFAULTS.items():
        val = data[0].get(key, default)
        if not isinstance(val, type(default)):
            print(f"Invalid value for '{key}', using default: {default}")
            config[key] = default
        else:
            config[key] = val

    return config
