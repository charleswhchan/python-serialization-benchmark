[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/charleswhchan/python-serialization-benchmark/master)

# python-serialization-benchmark
Performance comparison of different serialization formats with Python

[Launch interactive notebook](https://mybinder.org/v2/gh/charleswhchan/python-serialization-benchmark/master)

## FlatBuffers
- To re-generate schema for FlatBuffers: 
```
flatc --python FlatBuffersSchema/stations.fbs
```
- Then convert JSON to FlatBuffers binary format:
```
flatc --binary FlatBuffersSchema/stations.fbs stations.geojson && mv stations.bin FlatBuffersSchema/
```