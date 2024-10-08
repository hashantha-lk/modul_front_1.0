import json
import os

from local_settings import IMAGE_METER_CONFIG_PATH, IMAGE_METER_STYLE_PATH, MEASUREMENTS_JSON_FILENAME


def read_imagemeter_configuration() -> json:
    """
    Reads the configuration and style from file system
    :return:
    """
    configuration = {}
    with open(IMAGE_METER_CONFIG_PATH, "r") as f:
        # First load the configuration from the file system
        configuration = json.load(f)
        # Now try to load the styles configuration from the file system
        try:
            with open(IMAGE_METER_STYLE_PATH, "r") as sf:
                if configuration.get("algorithm", "pants") == "pants":
                    configuration["algoconfig"] = json.load(sf)
                else:
                    configuration["algoconfig"] = {}
        except Exception:
            pass
    return configuration


def measurement_statistics(measurement_folder: str) -> list:
    statistics = []
    digit_items = sorted(
        [int(x) for x in os.listdir(measurement_folder) if x.isdigit()], reverse=True
    )
    for measurement in digit_items:
        try:
            measurement_json = json.load(
                open(os.path.join(measurement_folder, str(measurement), MEASUREMENTS_JSON_FILENAME), "r")
            )
            statistics.append(
                {
                    "id": str(measurement),
                    "date": measurement_json.get("timestamp", ""),
                    "measurement_values": measurement_json.get("measures", {}),
                    "status": measurement_json.get("status", ""),
                    "algorithm": measurement_json.get("algorithm", "")
                }
            )
        except Exception:
            pass

    return statistics
