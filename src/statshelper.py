from scipy import stats

# Z Score

def convertPZfromAlpha2(alpha):
    """ 
    Parameters:
    -------
    - alpha: alpha value
    """

    return stats.norm.ppf(1-alpha/2)


def convertPZfromAlphaN(alpha, n_sided):
    """ 
    Parameters:
    -------
    - alpha: alpha value
    - n_sided: n sided
    """

    return stats.norm.ppf(1-alpha/n_sided)

def convertPZ(p):
    """ 
    Parameters:
    -------
    - p: p value
    """

    return stats.norm.ppf(p)


# T score

def convertT(alpha, n):
    """ 
    Parameters:
    -------
    - alpha: alpha value
    - n: sample size
    """

    return stats.t.ppf(1-(alpha/2), n-1)