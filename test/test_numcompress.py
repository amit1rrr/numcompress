import unittest
import random
import sys
import numpy as np
import pytest
from numcompress import compress, decompress, compress_ndarray, decompress_ndarray


class TestNumCompress(unittest.TestCase):

    def test_compress_decompress_works_for_single_int(self):
        series = [12345]
        text = '?qbW'
        self.assertEqual(compress(series, 0), text)
        self.assertEqual(decompress(text), series)

    def test_compress_decompress_works_in_lossy_fashion_for_longer_floats_when_enough_precision_not_spcified(self):
        original_series = [12365.54524354, 14789.54699, 11367.67845123]
        lossy_series = [12365.545, 14789.547, 11367.678]
        text = 'BqmvqVck}rCxizoE'
        self.assertEqual(compress(original_series), text)
        self.assertEqual(decompress(text), lossy_series)

    def test_compress_decompress_works_in_lossless_fashion_for_longer_floats_when_appropriate_precision_is_spcified(self):
        original_series = [12365.54524354, 14789.54673, 11367.67845987]
        text = 'Io{pcifu|_Folwenp}ak@f~itlgxf}@'
        self.assertEqual(compress(original_series, 10), text)
        self.assertEqual(decompress(text), original_series)

    def test_compression_ratio_for_series_of_epoch_timestamps(self):
        seed = 946684800  # start of year 2000
        series = [seed]
        previous = seed

        for _ in range(10000):
            current = previous + random.randrange(0, 600)
            series.append(current)
            previous = current

        original_size = sum(sys.getsizeof(i) for i in series)
        text = compress(series, 0)
        compressed_size = sys.getsizeof(text)
        reduction = ((original_size - compressed_size) * 100.0) / original_size

        self.assertEqual(compressed_size < original_size, True)
        print('10k timestamps compressed by ', round(reduction, 2), '%')

        self.assertEqual(decompress(text), series)

    def test_compression_ratio_for_series_of_floats(self):
        seed = 1247.53
        series = [seed]
        previous = seed

        for _ in range(10000):
            current = previous + random.randrange(1000, 100000) * (10**-2)
            series.append(round(current, 3))
            previous = current

        original_size = sum(sys.getsizeof(i) for i in series)
        text = compress(series)
        compressed_size = sys.getsizeof(text)
        reduction = ((original_size - compressed_size) * 100.0) / original_size

        self.assertEqual(compressed_size < original_size, True)
        print('10k floats compressed by ', round(reduction, 2), '%')

        self.assertEqual(decompress(text), series)

    def test_compress_none_value_raises_exception(self):
        with pytest.raises(ValueError):
            compress(None)

    def test_compress_non_list_value_raises_exception(self):
        with pytest.raises(ValueError):
            compress(23)

    def test_compress_decompress_works_with_empty_list(self):
        self.assertEqual(compress([]), '')
        self.assertEqual(decompress(''), [])

    def test_compress_non_numerical_list_value_raises_exception(self):
        with pytest.raises(ValueError):
            compress([123, 'someText', 456])

    def test_compress_non_integer_precision_raises_exception(self):
        with pytest.raises(ValueError):
            compress([123, 125], precision='someValue')

    def test_compress_negative_precision_raises_exception(self):
        with pytest.raises(ValueError):
            compress([123, 125], precision=-2)

    def test_compress_higher_than_limit_precision_raises_exception(self):
        with pytest.raises(ValueError):
            compress(23, precision=17)

    def test_decompress_non_text_input_raises_exception(self):
        with pytest.raises(ValueError):
            decompress(23)

    def test_decompress_invalid_text_input_raises_exception(self):
        with pytest.raises(ValueError):
            decompress('^fhfjelr;')

    def test_compress_decompress_works_with_numpy_array(self):
        series = np.random.randint(1, 100, 100).reshape(10, 10)
        assert (decompress_ndarray(compress_ndarray(series)) == series).all()