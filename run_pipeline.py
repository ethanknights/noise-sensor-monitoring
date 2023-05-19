import json
import time
import logging
import random


# Constants
STREAM_FREQUENCY = 2  # Frequency of the stream data in seconds
ALERT_COOLDOWN = 10  # Cooldown period for triggering alerts in seconds


def simulate_timeseries_stream():
    """Simulates a timeseries stream of decibel data."""
    # Simulate stream data
    while True:
        # Generate random decibel value
        if random.random() < 0.75:
            decibel = random.randint(30, 80)
        else:
            decibel = random.randint(81, 120)

        yield decibel
        time.sleep(STREAM_FREQUENCY)


def read_stream():
    """Reads the timeseries stream of decibel data."""
    stream = simulate_timeseries_stream()

    for decibel in stream:
        yield decibel


def check_data_length(data, min_length):
    """Checks the length of the data stream."""
    if len(data) < min_length:
        logging.warning(f"Data stream length ({len(data)}) is below the minimum threshold ({min_length})")


def check_missingness(data):
    """Checks for missing data in the stream."""
    if None in data:
        logging.warning("Missing data detected in the stream")


def check_anomaly(decibel, decibel_limit):
    """Checks if the decibel value breaches the limit."""
    if decibel > decibel_limit:
        logging.warning(f"Decibel breach detected! Current decibel ({decibel}) exceeds the limit ({decibel_limit})")


def read_decibel_limit():
    """Reads the decibel limit from a JSON file."""
    with open('decibel_limit.json') as file:
        data = json.load(file)
        return data['limit']


def log_breach():
    """Logs the decibel breach event."""
    logging.warning("Decibel breach event logged")


def trigger_alert(cooldown):
    """Triggers an event-related alert with cooldown."""
    logging.warning("Alert triggered")
    time.sleep(cooldown)


# Configure logging
log_filename = 'data.log'
logging.basicConfig(level=logging.WARNING, format="[%(asctime)s] [%(levelname)s] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")
file_handler = logging.FileHandler(log_filename, mode='a')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"))
file_handler.close_fds = True
logging.getLogger('').addHandler(file_handler)


# Read decibel limit
decibel_limit = read_decibel_limit()

# Initialize variables
data = []
last_alert_time = 0

# Start monitoring the stream
for decibel in read_stream():
    # Check data length and missingness
    data.append(decibel)
    check_data_length(data, min_length=10)
    check_missingness(data)

    # Check for decibel breach
    check_anomaly(decibel, decibel_limit)

    # Log breach and trigger alert (with cooldown)
    if decibel > decibel_limit and time.time() - last_alert_time >= ALERT_COOLDOWN:
        log_breach()
        trigger_alert(cooldown=5)
        last_alert_time = time.time()
