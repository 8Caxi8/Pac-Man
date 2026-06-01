from .parser import parser, ParserError


def main() -> None:
    try:
        config = parser()
        print(config)
    except ParserError as e:
        print(f"[ParserError]: {e}")


if __name__ == "__main__":
    main()
