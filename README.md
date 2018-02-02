# numcompress
Simple way to compress and decompress numerical series. Easily gets you above 80% compression. You can specify the precision you need (up to 10 decimal points). Efficient way to store, transmit series of numbers.

Compression algorithm is based on [google encoded polyline format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm). I tweaked it to preserve arbitrary precision and apply it to any numerical series. The work is motivated by usefulness of [time aware polyline](https://github.com/hypertrack/time-aware-polyline-py) built by [Arjun Attam](https://github.com/arjun27) at [HyperTrack](https://github.com/hypertrack/time-aware-polyline-py).

[![PyPI version](https://badge.fury.io/py/numcompress.svg)](https://badge.fury.io/py/numcompress) [![Build Status](https://travis-ci.org/amit1rrr/numcompress.svg?branch=master)](https://travis-ci.org/amit1rrr/numcompress)  [![Coverage Status](https://coveralls.io/repos/github/amit1rrr/numcompress/badge.svg)](https://coveralls.io/github/amit1rrr/numcompress)

# Installation
```
pip numcompress install
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


# Contribute
If you see any problem open an issue or send a pull request. You can write to [me](https://blog.amirathi.com/about/) at [amit.juschill@gmail.com](mailto:amit.juschill@gmail.com)
