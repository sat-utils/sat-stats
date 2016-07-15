# sat-stats

This utility library calculates zonal statistics on images being stored remotely on S3. Currently it uses the rasterstats package.

This requires GDAL2, which allows direct GDAL reading in S3 buckets.

For now, this is just calculating stats given an S3 key. However, the intention is that this could be a higher level library that uses sat-api and sat-search for calculating zonal stats on imagery stored on S3 file without downloading any data. It should be able to handle multiple vectors, vectors crossing tile/scene boundaries, and automatic handling of same regions but different dates as time series data.

