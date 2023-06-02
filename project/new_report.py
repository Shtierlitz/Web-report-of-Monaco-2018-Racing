# project/new_report.py

import os
from datetime import datetime


def read_abbr(file_path: str) -> dict[str, dict]:
    """Function that reads and forming up abbreviations"""
    res = {}
    with open(file_path, 'r', encoding="UTF-8") as f:
        for line in f.read().split("\n")[:-1]:
            abbr, name, team = line.split("_")
            res[abbr] = {abbr: [name, team]}

    return res


def read_log(time_path: str) -> dict[str]:
    """Function that reads and forming up time"""
    res = {}
    with open(time_path, 'r', encoding="UTF-8") as st:
        for line in st.read().split():
            time = datetime.strptime(line[3:], "%Y-%m-%d_%H:%M:%S.%f")
            res[line[0:3]] = time
    return res


def build_report(folder_path: str) -> dict[str, dict]:
    """Main build function"""
    abbrs = read_abbr(os.path.join(folder_path, 'abbreviations.txt'))
    starts = read_log(os.path.join(folder_path, 'start.log'))
    ends = read_log(os.path.join(folder_path, 'end.log'))

    for abbr, data in abbrs.items():
        pre_duration = ends[abbr] - starts[abbr]
        data["abbr"] = abbr
        data["name"] = data[abbr][0]
        data['team'] = data[abbr][1]
        data['start'] = str(starts[abbr])
        data['end'] = str(ends[abbr])
        duration = str(pre_duration) if len(str(pre_duration)) <= 14 else str(pre_duration)[8:]
        data['duration'] = duration

    return abbrs


def find_driver_by_abbr(report: dict, abbr: str):
    """Finds the complete dict of one rider"""
    return report.get(abbr, None)


def sort_report(report: dict, order: str) -> dict:
    """Sorts the report"""
    is_reversed = False
    if order == "desc":
        is_reversed = True
    return dict(sorted(report.items(), key=lambda item: item[1]['duration'], reverse=is_reversed))


def js_data_base_list(order):
    """Creates a json list from query"""
    js_lst = []
    for data in order:
        js_lst.append({
            'abbr': data.abbr,
            'duration': data.duration,
            'end': data.end,
            'name': data.name,
            "start": data.start,
            'team': data.team
        })
    return js_lst
