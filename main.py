import json
import logging
import argparse

from pathlib import Path

from uassetgen import JSON_to_uasset, UAsset_to_string

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

def main():

    parser = argparse.ArgumentParser(
        description="Patcher for the tags of DRG's DNA files. Used to add custom tags with the purpose of adding custom rooms."
    )
    parser.add_argument(
        "-c",
        "--config_path",
        nargs="?",
        default=Path("config") / "config.json",
        help="Path to the user configuration file. If not defined defaults to config/config.json.",
    )
    parser.add_argument(
        "-o",
        "--output_path",
        nargs="?",
        default="assets",
        help="Path where the patched DNA files will be written. If not specified defaults to assets/",
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Writes the patched UAsset in JSON form together with the output in the assets/ directory.",
    )
    args = parser.parse_args()
    
    try:
        with open(args.config_path, "r") as f:
            user_config_file = json.load(f)
        logging.info(f"Opening user configuration file: {args.config_path}")
    except OSError as e:
        logging.error(f"Error opening {args.config_path}: {e}")
        return 1
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing {args.config_path}: {e}")
        return 1
    
    # Some crude JSON validation:
    if "DNA" not in user_config_file:
        logging.error("Missing the DNA key in config file. Aborting.")
        return 1
    if "Tags" not in user_config_file:
        logging.error("No tags to substitute found in file. Aborting.")
        return 1

    for key, uasset_list in user_config_file["DNA"].items():
        for uasset in uasset_list:
            original_uasset_path = Path("assets") / "original" / uasset
            uasset_json = UAsset_to_string(original_uasset_path)
            for old_tag, new_tag in user_config_file["Tags"][key].items():
                uasset_json = uasset_json.replace(old_tag, new_tag)
            if args.debug:
                with open(f"assets/{uasset}.json", 'w') as f:
                    json.dump(json.loads(uasset_json), f, indent=4)
            try:
                write_path = Path(args.output_path) / uasset
                JSON_to_uasset(json.loads(uasset_json), write_path)
                logging.info(f"Written {uasset} to {write_path}")
            except Exception as e:
                logging.error(f"Error when writing asset {uasset}: {e}")
                continue

if __name__ == "__main__":
    main()
