[![PyPI version](https://badge.fury.io/py/numcompress.svg)](https://badge.fury.io/py/numcompress) [![Build Status](https://travis-ci.org/amit1rrr/numcompress.svg?branch=master)](https://travis-ci.org/amit1rrr/numcompress)  [![Coverage Status](https://coveralls.io/repos/github/amit1rrr/numcompress/badge.svg)](https://coveralls.io/github/amit1rrr/numcompress)

# numcompress
Simple way to compress and decompress numerical series.
 - Easily gets you above 80% compression ratio
 - You can specify the precision you need for floating points (up to 10 decimal points)
 - Useful to store or transmit stock prices, monitoring & other time series data in compressed string format

Compression algorithm is based on [google encoded polyline format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm). I modified it to preserve arbitrary precision and apply it to any numerical series. The work is motivated by usefulness of [time aware polyline](https://www.hypertrack.com/blog/2016/09/01/the-missing-dimension-in-geospatial-data-formats/) built by [Arjun Attam](https://github.com/arjun27) at [HyperTrack](https://github.com/hypertrack/time-aware-polyline-py).
After building this I came across [arrays](https://docs.python.org/3/library/array.html) that are much efficient than lists in terms memory footprint. You might consider using that over numcompress if you don't care about conversion to string for transmitting or storing purpose.

# Installation
```
pip install numcompress
```

# Usage
```python
from numcompress import compress, decompress

# Integers
>>> compress([14578, 12759, 13525])
'B_twxZnv_nB_bwm@'

>>> decompress('B_twxZnv_nB_bwm@')
[14578.0, 12759.0, 13525.0]



# precision argument specifies how many decimal points to preserve, defaults to 3

# Floats - lossless compression
>>> compress([145.7834, 127.5989, 135.2569], precision=4)
'Csi~wAhdbJgqtC'

>>> decompress('Csi~wAhdbJgqtC')
[145.7834, 127.5989, 135.2569]


# Floats - lossy compression
>>> compress([145.7834, 127.5989, 135.2569], precision=2)
'Acn[rpB{n@'

>>> decompress('Acn[rpB{n@')
[145.78, 127.6, 135.26]

# compressing and decompressing numpy arrays

>>> from numcompress import compress_ndarray, decompress_ndarray
>>> import numpy as np

>>> series = np.random.randint(1, 100, 100).reshape(10, 10)

>>> compress_ndarray(series)
'?S?,Bo|k@ojcA~kaAnqPnzD_qdBnqP_~i@n}}B_d_DninB~tu@_mV_uu@_}tAo}@nrbBosw@~yxA_fiAovs@ntiCoe`@_hpBn|hDojcA_{m@~zm@okXovs@~c_DocvB~uJ~rN_uu@owHnp{@ndkA_ieA_{m@ninBo_h@n}@o`zB~rkCoggA_yF_yFndkAo}}B~axBn_h@oe}C?ninB_bxB~wnDnzDom_Aoh\\nwH~|tA_{m@_|_C~wnD_|Bo_h@_ycCnnT_vJ~f^n{vA_|_C~pdBnggA_yFohyCntL~iwCowHodkAnxzA_rvD~ooC~xFne`@_}tA_db@njcAotLo{vAnnqC_{jD~lVninB_cmAnnTovs@~{BnqP'

>>> decompress_ndarray('?S?,Bo|k@ojcA~kaAnqPnzD_qdBnqP_~i@n}}B_d_DninB~tu@_mV_uu@_}tAo}@nrbBosw@~yxA_fiAovs@ntiCoe`@_hpBn|hDojcA_{m@~zm@okXovs@~c_DocvB~uJ~rN_uu@owHnp{@ndkA_ieA_{m@ninBo_h@n}@o`zB~rkCoggA_yF_yFndkAo}}B~axBn_h@oe}C?ninB_bxB~wnDnzDom_Aoh\\nwH~|tA_{m@_|_C~wnD_|Bo_h@_ycCnnT_vJ~f^n{vA_|_C~pdBnggA_yFohyCntL~iwCowHodkAnxzA_rvD~ooC~xFne`@_}tA_db@njcAotLo{vAnnqC_{jD~lVninB_cmAnnTovs@~{BnqP').shape
(10, 10)
```


# Compression Ratio

| Test          | # of Numbers          | Compression ratio |
| ------------- |-------------- |---------------------------|
| [Integers](https://github.com/amit1rrr/numcompress/blob/master/test/test_numcompress.py#L29)    | 10k | **91.14%** |
| [Floats](https://github.com/amit1rrr/numcompress/blob/master/test/test_numcompress.py#L49)      | 10k | **81.35%** |

You can run the test suite with -s switch to see the compression ratio. You can even modify the tests to see what kind of compression ratio you will get for your own input.
```
pytest -s
```

Here's a quick example showing compression ratio:

```python
>>> series = random.sample(range(1, 100000), 50000)  # generate 50k random numbers between 1 and 100k
>>> text = compress(series)  # apply compression

>>> original_size = sum(sys.getsizeof(i) for i in series)
>>> original_size
1200000

>>> compressed_size = sys.getsizeof(text)
>>> compressed_size
284092

>>> compression_ratio = ((original_size - compressed_size) * 100.0) / original_size
>>> compression_ratio
76.32566666666666
```

We get ~76% compression for 50k random numbers between 1 & 100k. This ratio increases for real world numerical series as the difference between consecutive numbers tends to be lower. Think of stock prices, monitoring & other time series data.


# Contribute
If you see any problem, open an issue or send a pull request. You can write to [me](https://blog.amirathi.com/about/) at [amit.juschill@gmail.com](mailto:amit.juschill@gmail.com)
