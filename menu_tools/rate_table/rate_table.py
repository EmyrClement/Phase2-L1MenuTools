import argparse
import yaml

from menu_tools.rate_table.menu_table import MenuTable


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "config_file",
        help="Path to the menu config file, e.g. `configs/V29/rate_table/v29_cfg.yml`",
    )
    args = parser.parse_args()

    with open(args.config_file, "r") as f:
        menu_config_dict = yaml.safe_load(f)

    menu_table = MenuTable(menu_config_dict)
    table = menu_table.make_table()
    menu_table.dump_table(table)
    menu_table.dump_masks()


if __name__ == "__main__":
    main()
