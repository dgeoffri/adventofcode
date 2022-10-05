#!/usr/bin/env python

import itertools

def extract_rules(inputdata):
    rules = {}
    line = inputdata.pop(0)
    while len(line):
        rule, ranges = line.split(": ")
        rules[rule] = tuple(tuple(map(int, range.split("-"))) for range in ranges.split(" or "))
        line = inputdata.pop(0)
    return rules

def extract_tickets(inputdata):
    ticketdict = {}
    line = inputdata.pop(0)
    while len(line):
        ticketholder, restofline = line.split()
        assert restofline.startswith("ticket")
        tickets = []
        line = inputdata.pop(0)
        while len(line):
            tickets.append(map(int, line.split(',')))
            if len(inputdata):
                line = inputdata.pop(0)
            else:
                line = ""
        ticketdict[ticketholder] = tickets
        if len(inputdata):
            line = inputdata.pop(0)
        else:
            line = ""
    return ticketdict

def find_errors_in_tickets(rules, tickets):
    concat_rules = list(itertools.chain(*rules.values()))
    errors_in_tickets = []
    for ticket in tickets:
        errors_in_ticket = []
        for value in ticket:
            rule_matched = False
            for min, max in concat_rules:
                if (min <= value <= max):
                    rule_matched = True
                    continue
            if not rule_matched:
                errors_in_ticket.append(value)
        errors_in_tickets.append(errors_in_ticket)
    return errors_in_tickets

def ticket_is_valid_factory(rules):
    concat_rules = list(itertools.chain(*rules.values()))
    def ticket_is_valid(ticket):
        valid_ticket = True
        for value in ticket:
            rule_matched = False
            for min, max in concat_rules:
                if (min <= value <= max):
                    rule_matched = True
                    continue
            if not rule_matched:
                valid_ticket = False
                continue
        return valid_ticket
    return ticket_is_valid

def field_is_valid(rules, fieldvalue):
    for min, max in rules:
        if (min <= fieldvalue <= max):
            return True
    return False

def prune(mappings, column_to_remove):
    for field in mappings:
        if field == fieldname:
            continue
        if len(mappings[field]) > 1:
            mappings[field].remove(column_to_remove)
            if len(mappings[field]) == 1:
                # Recurse
                prune(mappings, mappings[field][0])

if __name__ == "__main__":
    with open('day16.txt', 'r') as f:
        inputdata = f.read().splitlines()
    rules = extract_rules(inputdata)
    ticketdict = extract_tickets(inputdata)
    goodtickets = filter(ticket_is_valid_factory(rules), ticketdict['nearby'] + ticketdict['your'])
    possible_mappings = { key: list(range(len(ticketdict['nearby'][0]))) for key in rules }

    for ticketnumber, ticket in enumerate(goodtickets):
        for column_number, value in enumerate(ticket):
            for fieldname, rule in rules.items():
                if column_number in possible_mappings[fieldname] and not field_is_valid(rule, value):
                    possible_mappings[fieldname].remove(column_number)
                    if len(possible_mappings[fieldname]) == 1:
                        column_to_remove = possible_mappings[fieldname][0]
                        # positive allocation, remove this choice from the rest
                        prune(possible_mappings, column_to_remove)

    product = 1
    myticket = ticketdict['your'][0]
    for fieldname in possible_mappings:
        if fieldname.startswith("departure"):
            fieldnumber = possible_mappings[fieldname][0]
            product *= myticket[fieldnumber]
    print "Part b answer is: " + str(product)

#  'row': ((32, 789), (795, 955))