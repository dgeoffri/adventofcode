#!/usr/bin/env python

def has_required_fields(passport):
    valid = True
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if not field in passport.keys():
            valid = False
            break
    return(valid)

def is_valid(passport):
    try:
        if not passport['byr'].isdigit() or int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
            return False
        if not passport['iyr'].isdigit() or int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
            return False
        if not passport['eyr'].isdigit() or int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
            return False
        hgt = passport['hgt']
        if hgt.endswith('cm'):
            if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
                return False
        elif hgt.endswith('in'):
            if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
                return False
        else:
            return False
        if not passport['hcl'].startswith("#") or not reduce(lambda i, j: i & j, map(lambda x: x in '0123456789abcdef', passport['hcl'][1:])):
            return False
        if not passport['ecl'] in "amb blu brn gry grn hzl oth".split():
            return False
        if not (len(passport['pid']) == 9) or not passport['pid'].isdigit():
            return False
        return True
    except KeyError:
        return False

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
    records_with_required_fields = filter(has_required_fields, records)
    print "{} of {} passports have all the required fields.".format(len(records_with_required_fields), len(records))
    valid_records = filter(is_valid, records_with_required_fields)
    print "Of those, {} are also valid.".format(len(valid_records))