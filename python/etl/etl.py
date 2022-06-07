def transform(legacy_data):
    result = {}
    for i in legacy_data:
        for j in legacy_data[i]:
            result[j.lower()] = i
    return dict(sorted(result.items()))


