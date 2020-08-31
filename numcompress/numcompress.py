import numpy as np

PRECISION_LOWER_LIMIT = 0
PRECISION_UPPER_LIMIT = 10

# Used for N-Dimensional array. Separates dimension and the series.
# Should have ASCII value between (0, 63) to avoid overlapping with regular compress output.
SEPARATOR = ','


def compress(series, precision=3):
    last_num = 0
    result = ''

    if not isinstance(series, list):
        raise ValueError('Input to compress should be of type list.')

    if not isinstance(precision, int):
        raise ValueError('Precision parameter needs to be a number.')

    if precision < PRECISION_LOWER_LIMIT or precision > PRECISION_UPPER_LIMIT:
        raise ValueError('Precision must be between 0 to 10 decimal places.')

    is_numerical_series = all(isinstance(item, int) or isinstance(item, float) for item in series)

    if not is_numerical_series:
        raise ValueError('All input list items should either be of type int or float.')

    if not series:
        return result

    # Store precision value at the beginning of the compressed text
    result += chr(precision + 63)

    for num in series:
        diff = num - last_num
        diff = int(round(diff * (10 ** precision)))
        diff = ~(diff << 1) if diff < 0 else diff << 1

        while diff >= 0x20:
            result += (chr((0x20 | (diff & 0x1f)) + 63))
            diff >>= 5

        result += (chr(diff + 63))
        last_num = num

    return result


def decompress(text):
    result = []
    index = last_num = 0

    if not isinstance(text, str):
        raise ValueError('Input to decompress should be of type str.')

    if not text:
        return result

    # decode precision value
    precision = ord(text[index]) - 63
    index += 1

    if precision < PRECISION_LOWER_LIMIT or precision > PRECISION_UPPER_LIMIT:
        raise ValueError('Invalid string sent to decompress. Please check the string for accuracy.')

    while index < len(text):
        index, diff = decompress_number(text, index)
        last_num += diff
        result.append(last_num)

    result = [round(item * (10 ** (-precision)), precision) for item in result]
    return result


def decompress_number(text, index):
    result = 1
    shift = 0

    while True:
        b = ord(text[index]) - 63 - 1
        index += 1
        result += b << shift
        shift += 5

        if b < 0x1f:
            break

    return index, (~result >> 1) if (result & 1) != 0 else (result >> 1)


def compress_ndarray(series, precision=3):
    shape = "*".join(map(str, series.shape))
    series_compressed = compress(series.flatten().tolist(), precision)
    return '{}{}{}'.format(shape, SEPARATOR, series_compressed )


def decompress_ndarray(text):
    shape_str, series_text = text.split(SEPARATOR)
    shape = tuple(int(dimension) for dimension in shape_str.split('*'))
    series = decompress(series_text)
    return np.array(series).reshape(*shape)
