def compress(series, precision=5):
    last_num = 0
    result = ''

    if not isinstance(series, list):
        raise ValueError('Input to compress should be of type list.')

    if not isinstance(precision, int):
        raise ValueError('Precision parameter needs to be a number.')

    is_numerical_series = all(isinstance(item, int) or isinstance(item, float) for item in series)

    if not is_numerical_series:
        raise ValueError('All input list items should either be of type int or float.')

    for num in series:
        diff = num - last_num
        diff = int(round(diff * (10**precision)))
        diff = ~(diff << 1) if diff < 0 else diff << 1

        while diff >= 0x20:
            result += (chr((0x20 | (diff & 0x1f)) + 63))
            diff >>= precision

        result += (chr(diff + 63))
        last_num = num

    return result


def decompress(text, precision=5):
    result = []
    index = last_num = 0

    if not isinstance(text, basestring):
        raise ValueError('Input to decompress should be of type str.')

    while index < len(text):
        index, diff = decompress_number(text, index, precision)
        last_num += diff
        result.append(last_num)

    result = [round(item * (10 ** (-precision)), precision) for item in result]
    return result


def decompress_number(text, index, precision):
    result = 1
    shift = 0

    while True:
        b = ord(text[index]) - 63 - 1
        index += 1
        result += b << shift
        shift += precision

        if b < 0x1f:
            break

    return index, (~result >> 1) if (result & 1) != 0 else (result >> 1)
