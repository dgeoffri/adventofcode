#!/usr/bin/env python

def has_required_fields(passport):
    valid = True
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if not field in passport.keys():
            valid = False
            break
    return(valid)

if __name__ == "__main__":
    with open('day04.txt', 'r') as f:
        record = {}
        records = []
        for line in f.read().split('\n\n'):
            for attr in line.split():
                key, val = attr.split(":")
                record[key] = val
            records.append(record)
            record = {}
    valid_records = filter(has_required_fields, records)
    print "{} of {} passports have all the required fields.".format(len(valid_records), len(records))
