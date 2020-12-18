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

if __name__ == "__main__":
    with open('day16.txt', 'r') as f:
        inputdata = f.read().splitlines()
    rules = extract_rules(inputdata)
    ticketdict = extract_tickets(inputdata)
    errors_in_tickets = find_errors_in_tickets(rules, ticketdict['nearby'])
    print sum(itertools.chain(*(filter(len, errors_in_tickets))))
