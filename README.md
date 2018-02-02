[![PyPI version](https://badge.fury.io/py/numcompress.svg)](https://badge.fury.io/py/numcompress) [![Build Status](https://travis-ci.org/amit1rrr/numcompress.svg?branch=master)](https://travis-ci.org/amit1rrr/numcompress)  [![Coverage Status](https://coveralls.io/repos/github/amit1rrr/numcompress/badge.svg)](https://coveralls.io/github/amit1rrr/numcompress)

# numcompress
Simple way to compress and decompress numerical series.
 - Easily gets you above 80% compression ratio
 - You can specify the precision you need for floating points (up to 10 decimal points)
 - Provides an efficient way to store or transmit series of numbers in a compressed string format

Compression algorithm is based on [google encoded polyline format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm). I modified it to preserve arbitrary precision and apply it to any numerical series. The work is motivated by usefulness of [time aware polyline](https://github.com/hypertrack/time-aware-polyline-py) built by [Arjun Attam](https://github.com/arjun27) at [HyperTrack](https://github.com/hypertrack/time-aware-polyline-py).


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

```


# Compression Ratio
[This](https://github.com/amit1rrr/numcompress/blob/master/test/test_numcompress.py#L29) and [this](https://github.com/amit1rrr/numcompress/blob/master/test/test_numcompress.py#L49) test computes compression ratio. We get **91.14%** compression for 10k integers and **81.35%** compression for 10k floats. You can run the test suite with -s switch to see the compression ratio.
```
pytest -s
```

# Contribute
If you see any problem, open an issue or send a pull request. You can write to [me](https://blog.amirathi.com/about/) at [amit.juschill@gmail.com](mailto:amit.juschill@gmail.com)
