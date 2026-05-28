def calculate_late_fee(days):

    if days > 15:
        return (days - 15) * 50

    return 0