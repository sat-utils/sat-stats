from rasterstats import zonal_stats

def get_stats(s3key, vectors):
    """ Retrieve stats from image for vectors """
    stats = zonal_stats(vectors, s3key)
    return stats
