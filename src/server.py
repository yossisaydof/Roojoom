
def check_indicator(indicators, status):
    for indicator in indicators:
        if indicator.lower() != status:
            return False

    return True


def get_response_status(created_problem):
    serial_number = created_problem.get('serial_number')
    status_indicator1 = created_problem.get('status_indicator1')
    status_indicator2 = created_problem.get('status_indicator2')
    status_indicator3 = created_problem.get('status_indicator3')

    if serial_number.isdigit():
        return "Bad serial number"

    serial_number_list = serial_number.split("-")
    if len(serial_number_list) < 2:
        return "Bad serial number"

    first, second, *_ = serial_number_list
    serial_number_start = "-".join([first, second])

    if serial_number_start == "24-X":
        return "please upgrade your device"

    elif serial_number_start == "36-X":
        if check_indicator([status_indicator1, status_indicator2, status_indicator3], "off"):
            return "turn on the device"
        if check_indicator([status_indicator1, status_indicator2], "blinking"):
            return "Please wait"
        if check_indicator([status_indicator1, status_indicator2, status_indicator3], "on"):
            return "ALL is ok"

    elif serial_number_start == "51-B":
        if check_indicator([status_indicator1, status_indicator2, status_indicator3], "off"):
            return "turn on the device"
        if check_indicator([status_indicator1], "blinking"):
            return "Please wait"

        if check_indicator([status_indicator1], "on") and \
                check_indicator([status_indicator2, status_indicator3], "off"):
            return "ALL is ok"
        if check_indicator([status_indicator2], "on") and \
                check_indicator([status_indicator1, status_indicator3], "off"):
            return "ALL is ok"
        if check_indicator([status_indicator3], "on") and \
                check_indicator([status_indicator1, status_indicator2], "off"):
            return "ALL is ok"

    return "Unknown device"
