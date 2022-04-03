def detect(utilizations):
    last = len(utilizations) - 1
    # 0 usage
    if utilizations[last] <= 1 and utilizations[last - 1] <= 1 and utilizations[last - 2] <= 1:
        return "empty_server"
    # low usage
    if utilizations[last] <= 30 and utilizations[last - 1] <= 30 and utilizations[last - 2] <= 30:
        return "change_server_host"
    # calculate m
    m = utilizations[last] - utilizations[last - 1] / utilizations[last - 1] - utilizations[last - 2]

    # high m based on the prev one
    if m >= 2:
        return "hacked"
    # low m based on the prev one
    if m <= -2:
        return "server_cooled_hard"
    # normal
    return "normal_status"