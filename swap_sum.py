def histogram(points, bins):
    """Efficiently computes a histogram.

    Assumes that both `points` and `bins` are sorted in ascending order to
    avoid looping through all bins for each point.

    """
    n = len(points)
    counts = [0] * len(bins)
    
    bin_idx = 0
    for point in points:
        while point >= bins[bin_idx][1]:
            bin_idx += 1
        counts[bin_idx] += 1
    
    return [counts[i] / (n * (bins[i][1] - bins[i][0])) for i in range(len(bins))]