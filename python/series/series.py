def slices(series, length):
    series_length = len(series)
    if length > series_length:
        raise ValueError(f"Series length {series_length} is less than requested substring length {length}.")
    if length <= 0:
        raise ValueError(f"Substring length {length} must be positve")
    index = 0
    results = []
    while index + length <= series_length:
        results.append(series[index:length+index])
        index += 1
    return results

""""
def slices(series, length):
    if series == '':
        raise ValueError('Series cannot be empty.')
    if length <= 0:
        raise ValueError('Length has to be larger than zero.')
    if length > len(series):
        raise ValueError('Requested slice cannot be longer than series.')

    return [series[i:length+i] for i in range(len(series)-(length-1))]
"""