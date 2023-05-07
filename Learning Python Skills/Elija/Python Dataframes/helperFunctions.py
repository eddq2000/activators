def millisToSeconds(milli, reference):
    """Description of Function
    
    Parameters:
    milli (int): A time represented in milli-seconds
    reference: A time represented in milli-seconds, which marks the 0 timestamp for a time series

    Returns:
    float: time in seconds relative to the reference time point
    """
    return (float(milli) - float(reference)) / 1000