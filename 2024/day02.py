#!/usr/bin/env python3

import sys

DAY = 2
SAMPLE_DATA = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

def solve_pt1(inputfile):
    def is_safe(report):
        direction = 0
        last_level = report[0]
        for i in range(1, len(report)):
            if not direction:
                if report[i] > last_level:
                    direction = 1
                elif report[i] < last_level:
                    direction = -1
                else:
                    return False
            if direction == 1:
                difference = report[i] - last_level
            else:
                difference = last_level - report[i]
            # print(f"difference = {difference}")
            if (difference < 1) or (difference > 3):
                return False
            last_level = report[i]
        return True
    reports = []
    for line in inputfile:
        reports.append(list(map(int, line.strip().split())))
    safe_reports = [report for report in reports if is_safe(report)]
    # print(f"safe reports: {safe_reports}")    
    print(f"{len(safe_reports)} reports are safe")    

def solve_pt2(inputfile):
    def is_safe2(report, deletion=None):
        if deletion is not None:
            old_report = report
            report = old_report.copy()
            report.pop(deletion)
        direction = 0
        last_level = report[0]
        for i in range(1, len(report)):
            if not direction:
                if report[i] > last_level:
                    direction = 1
                elif report[i] < last_level:
                    direction = -1
                else:
                    return False
            if direction == 1:
                difference = report[i] - last_level
            else:
                difference = last_level - report[i]
            # print(f"difference = {difference}")
            if (difference < 1) or (difference > 3):
                return False
            last_level = report[i]
        return True
    def is_safe(report):
        if is_safe2(report, None):
            return True
        for i in range(0, len(report)):
            if is_safe2(report, i):
                return True
        return False
    reports = []
    for line in inputfile:
        reports.append(list(map(int, line.strip().split())))
    safe_reports = [report for report in reports if is_safe(report)]
    # print(f"safe reports: {safe_reports}")    
    print(f"{len(safe_reports)} reports are safe")    

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-e":
        from io import StringIO
        puzzle_input = StringIO(SAMPLE_DATA)
    else:
        try:
            puzzle_input = open("day{:02d}.txt".format(DAY), "r")
        except OSError as e:
            print("Something went horribly wrong: {}".format(e))
            sys.exit(1)

    with puzzle_input as f:
        print("---PART 1---")
        solve_pt1(f)
        f.seek(0)
        print("\n---PART 2---")
        solve_pt2(f)
