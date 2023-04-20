import os
from datetime import datetime
from logging import Logger


def screenshot(driver, msg=""):
    now = datetime.now(format="%H:%M:%S")
    file_name = f"{msg}_{now}.png"
    screenshot_dir = "../screenshots/"
    current_dir = os.path.dirname(__file__)
    destination_dir = os.path.join(current_dir, screenshot_dir)
    destination_file = os.path.join(destination_dir, file_name)
    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        driver.save_screenshot(destination_file)
        Logger.info(f"Screenshot save to directory: {destination_file}")
    except Exception as e:
        Logger.error(f"# Exception: Exception Occurred when taking screenshot, {e}")
    return destination_file
