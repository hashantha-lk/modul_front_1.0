# ImageMeter settings
IMAGE_METER_TRY_RUNS = 5
IMAGE_METER_MESSAGE_QUEUE_IPC_KEY = 12345
IMAGE_METER_OUTGOING_MESSAGE_TYPE = 0x01010101
IMAGE_METER_INCOMING_MESSAGE_TYPE = 0x02020202
# Path to the ImageMeter Software
IMAGE_METER_LOCAL_PATH = "./imagemeter-pants-v0.3.0-x86_64.AppImage"
# Path to the ImageMeter PID-file
IMAGE_METER_PID_PATH = "./imagemeter.pid"
# Path to ImageMeter config-file
IMAGE_METER_CONFIG_PATH = "./imagemeter.config.json"
# Path to ImageMeter style-file
IMAGE_METER_STYLE_PATH = "./imagemeter.style.json"
# Path to local calibration folder that is always placed inside the ImageMeter folder
IMAGE_METER_CALIBRATION_PATH = "./new_canvas-copy-3"
# Measurements settings
MEASUREMENTS_SUBFOLDER_DIR = "measurements"
MEASUREMENTS_SNAPSHOT_FILENAME = "snapshot.jpg"
MEASUREMENTS_JSON_FILENAME = "measurement.json"

MEASUREMENT_ALGORITHMS_WITH_METHODS = {
    "pants": [
        "half-waist-width", "half-hip-width", "lower-border", "side-length-left", "side-length-right",
        "reduced-side-left", "reduced-side-right", "length-to-seam", "gusset-length",
        "middle-length", "half-leg-opening", "gusset-width"
    ],
    "tshirts": [
        "sleeve-left", "sleeve-right", "bottom-width", "axle-width", "neck-width",
        "sleeve-to-shoulder-left", "sleeve-to-shoulder-right", "shoulder-width",
        "neck-to-bottom-left", "neck-to-bottom-right"
    ]
}

MEASUREMENT_ALGORITHMS = list(MEASUREMENT_ALGORITHMS_WITH_METHODS.keys())

MEASUREMENT_COLOR_MODES = ["black-on-white", "white-on-black"]
