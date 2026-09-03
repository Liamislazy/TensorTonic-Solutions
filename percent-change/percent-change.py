def percent_change(series: list) -> list:
    """
    Returns the fractional change between consecutive values.
    """
    diff_percent = []
    for i in range(len(series)-1):
        if series[i] == 0:
            diff_percent.append(0.0)
        else:
            diff_percent.append(float((series[i+1] - series[i]) / series[i]))
    return diff_percent