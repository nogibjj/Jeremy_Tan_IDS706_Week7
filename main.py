"""handles cli commands"""
import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    general_query,
)


def handle_arguments(args):
    """add action based on inital calls"""
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "transform_load",
            "general_query",
        ],
        # shows how to run output
        help="""Action to perform (extract, transform_load, general_query). 
        \u5927\u5bb6\u597d\uff0c\u8c22\u8c22\u4f60\u4eec\u4f7f\u7528\u6211
        \u7684\u4ee3\u7801\u3002\u4e0b\u6b21\u8bf7\u95ee\u6211\u3002""",
    )
    args = parser.parse_args(args[:1])
    if args.action == "general_query":
        parser.add_argument("query")

    # parse again with ever
    return parser.parse_args(sys.argv[1:])


def main():
    """handles all the cli commands"""
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract()
    elif args.action == "transform_load":
        print("Transforming data...")
        load()
    elif args.action == "general_query":
        general_query(args.query)
        # fixes output so need to include this
        print(
            "\u5927\u5bb6\u597d\uff0c\u8c22\u8c22\u4f60"
            + "\u4eec\u4f7f\u7528\u6211\u7684\u4ee3\u7801\u3002\u4e0b"
            + "\u6b21\u8bf7\u95ee\u6211\u3002\n\n"
        )

    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
