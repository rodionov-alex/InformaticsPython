def check_way(data: dict, way: str, cur_point: str, end: str):
    if cur_point == end:
        return 1
    elif cur_point in way:
        return 0

    way += cur_point
    res = 0

    for w in data[cur_point]:
        res += check_way(data, way, w, end)

    return res


def count_ways(data: dict, begin: str, end: str):
    res = 0

    for w in data[begin]:
        res += check_way(data, begin, w, end)

    return res


roads = dict()
roads['А'] = 'Б'
roads['Б'] = 'В'
roads['В'] = 'ГЕЖ'
roads['Г'] = 'ЕД'
roads['Д'] = 'ЕЖК'
roads['Е'] = 'Ж'
roads['Ж'] = 'ЗН'
roads['З'] = 'ЛКД'
roads['К'] = 'Л'
roads['Л'] = 'М'
roads['М'] = 'АНЗ'
roads['Н'] = 'АБВ'

print(count_ways(roads, 'Ж', 'Ж'))
