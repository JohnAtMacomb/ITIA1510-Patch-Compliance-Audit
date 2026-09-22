"""
Week 06 INDIVIDUAL ASSIGNMENT -- Patch Compliance Audit
ITIA 1510 Cybersecurity Automation

Topic: lists, from Week 05, and everything before them. Input and output,
if / elif / else, while and for loops, functions that return values, and
debugging. No dictionaries.

This program reads the patch inventory, gives every host a status against the
patch policy, and reports how much of the network is inside that policy.

THE POLICY
   Criticality 3 (domain controllers, databases)   patch within 14 days
   Criticality 2 (servers)                          patch within 30 days
   Criticality 1 (workstations, kiosks, printers)   patch within 60 days

   COMPLIANT   days since patch is no more than the limit
   OVERDUE     past the limit, but no more than twice the limit
   CRITICAL    more than twice the limit
   EXEMPT      the host is on the signed exception list, whatever its numbers say
   INVALID     the record cannot be trusted: days below 0, or a criticality
               that is not 1, 2 or 3

The inventory, the section headings and the input checks are already written.
Work through the 20 numbered TODOs in order. Two of the functions are finished
and wrong, and fixing them is part of the job.

Run the file before changing anything. It works, but every answer is wrong,
because every function still returns a placeholder.

The host names are invented.
"""

# The inventory is three PARALLEL LISTS. Position 0 in each list describes the
# same host, position 1 the next host, and so on.
HOSTS = [
    "dc-01", "dc-02", "web-01", "web-02", "db-01", "mail-01", "file-01",
    "hr-laptop-07", "kiosk-03", "lab-sandbox-01", "lab-sandbox-02",
    "print-01", "vpn-01",
]
DAYS_SINCE_PATCH = [9, 31, 12, 45, 95, 30, 61, 130, 58, 400, -1, -1, 20]
CRITICALITY = [3, 3, 2, 2, 3, 2, 1, 1, 1, 1, 1, 1, 0]

# Hosts with a signed exception. They are left out of the compliance rate.
EXEMPT = ["lab-sandbox-01", "lab-sandbox-02"]

# The order the summary prints in.
STATUS_ORDER = ["COMPLIANT", "OVERDUE", "CRITICAL", "EXEMPT", "INVALID"]


# ---------------------------------------------------------------------------
# One host at a time
# ---------------------------------------------------------------------------

def patch_limit(criticality):
    """Return the number of days the policy allows: 14, 30 or 60."""
    # TODO 1
    #   Criticality 3 gets 14 days, criticality 2 gets 30, anything else 60.
    return 0


def is_valid_record(days, criticality):
    """True when days is 0 or more AND criticality is 1, 2 or 3."""
    # TODO 2
    #   One return statement. Say the rule in English before writing it, and
    #   decide where it needs and, and where it needs or.
    return False


def patch_status(host, days, criticality, exempt):
    """Return 'EXEMPT', 'INVALID', 'COMPLIANT', 'OVERDUE' or 'CRITICAL'."""
    # TODO 3
    #   Build this out of is_valid_record and patch_limit. It should not
    #   contain the numbers 14, 30 or 60.
    #   The order of the branches matters. lab-sandbox-02 has a broken record
    #   AND a signed exception. The policy says which one wins.
    return "INVALID"


def days_overdue(days, criticality):
    """Return how many days past the limit a host is, or 0 when it is not."""
    # TODO 4
    #   Never return a negative number.
    return 0


def overdue_bar(overdue):
    """Return a bar of # characters, one for every 10 full days overdue."""
    # TODO 5
    #   81 days overdue is "########". Use // and string replication.
    #   A host that is overdue at all gets at least one #, so 1 day is "#".
    #   No bar is longer than 10 characters. 0 days overdue is "".
    return ""


def will_lapse(days, criticality, days_ahead):
    """True when a host is inside its limit today but will be past it
    days_ahead days from now, if nobody patches it."""
    # TODO 6
    return False


# ---------------------------------------------------------------------------
# The whole inventory
# ---------------------------------------------------------------------------

def build_statuses(hosts, days, crits, exempt):
    """Return a new list holding the status of every host, in the same order."""
    # TODO 7
    #   The three lists are parallel, so loop over the POSITIONS with
    #   range(len(hosts)) and use the position to reach into all three.
    #   Append each status to a new list and return the list.
    #   Remember what append() returns before writing  x = x.append(y).
    return []


def count_status(statuses, wanted):
    """Return how many entries in statuses equal wanted."""
    # TODO 8
    #   Write the loop and the counter. Do not use the .count() method.
    return 0


def hosts_with_status(hosts, statuses, wanted):
    """Return a list of the host names whose status equals wanted."""
    # TODO 9
    return []


def worst_host(hosts, days, crits, statuses):
    """Return the POSITION of the host that is the most days overdue, looking
    only at hosts whose status is OVERDUE or CRITICAL. Return -1 when no host
    has either status."""
    # TODO 10
    #   Keep a best-so-far position and a best-so-far number of days overdue,
    #   and update both whenever a host beats them.
    #   The most days since patch and the most days OVERDUE are not the same
    #   host in this inventory. The policy is why.
    return -1


def remove_exempt(hosts, exempt):
    """Return a copy of hosts with every exempt host taken out."""
    # TODO 11 -- DEBUG
    #   This function is finished and it is wrong. The inventory holds 13
    #   hosts and 2 are exempt, so it should return 11. It returns 12.
    #   Set a breakpoint, step through the loop and watch remaining and host.
    #   Find out which host survives and why, then fix the function.
    remaining = hosts[:]
    for host in remaining:
        if host in exempt:
            remaining.remove(host)
    return remaining


def average_days(days, statuses):
    """Return the average days since patch, leaving out EXEMPT and INVALID
    hosts, rounded to 1 decimal place."""
    # TODO 12 -- DEBUG
    #   This function is finished and it is wrong in TWO places. The right
    #   answer for this inventory is 52.3. Work the average out by hand for
    #   the first three hosts, then step through and find where the function
    #   disagrees with you. It cannot be tested until TODO 7 is done.
    total = 0
    for i in range(1, len(statuses)):
        if statuses[i] != "EXEMPT" and statuses[i] != "INVALID":
            total = total + days[i]
    return round(total / len(days), 1)


# ---------------------------------------------------------------------------
# The report
# ---------------------------------------------------------------------------

# The report runs only when this file is run directly, so the test file can
# import the functions above without the report printing or asking for input.
if __name__ == "__main__":
    statuses = build_statuses(HOSTS, DAYS_SINCE_PATCH, CRITICALITY, EXEMPT)

    print("=" * 66)
    print("PATCH COMPLIANCE AUDIT")
    print("=" * 66)
    print("Hosts in the inventory:   " + str(len(HOSTS)))
    print("Hosts that are audited:   " + str(len(remove_exempt(HOSTS, EXEMPT))))

    print()
    print("-" * 66)
    print("HOST".ljust(18) + "CRIT".ljust(6) + "DAYS".ljust(7) + "STATUS".ljust(11) + "OVERDUE")
    print("-" * 66)
    # TODO 13
    #   Print one line for every host, lined up under the headings above, using
    #   the same .ljust() widths the heading line uses. Numbers need str() first.
    #   The last column is the overdue_bar for the host. Print a bar only when the
    #   status is OVERDUE or CRITICAL. An exempt host is 340 days past its limit
    #   and still gets no bar.

    print()
    print("-" * 66)
    print("SUMMARY")
    print("-" * 66)
    # TODO 14
    #   Walk STATUS_ORDER and print each status with its count from count_status,
    #   so the summary always prints in the same order and a status nobody has
    #   still shows 0. Use .ljust(12) on the status.

    # TODO 15
    #   The compliance rate is the COMPLIANT hosts as a percentage of the hosts
    #   that can be judged: every host that is not EXEMPT and not INVALID.
    #   Round it to 1 decimal place. If no host can be judged, the rate is 0.0,
    #   and the program must not crash on the division.
    rate = 0.0

    # TODO 16
    #   The verdict is PASS at a rate of 90 or above, AT RISK at 70 or above, and
    #   FAIL below that. The order the branches are tested in matters.
    verdict = "UNKNOWN"

    print()
    print("Compliance rate:          " + str(rate) + "%")
    print("Audit verdict:            " + verdict)
    print("Average days since patch: " + str(average_days(DAYS_SINCE_PATCH, statuses)))

    worst = worst_host(HOSTS, DAYS_SINCE_PATCH, CRITICALITY, statuses)
    if worst == -1:
        print("Most overdue host:        none")
    else:
        print("Most overdue host:        " + HOSTS[worst] + " ("
              + str(days_overdue(DAYS_SINCE_PATCH[worst], CRITICALITY[worst]))
              + " days past its limit)")

    print()
    print("-" * 66)
    print("ESCALATION QUEUE")
    print("-" * 66)
    # TODO 17
    #   The patch team takes 3 tickets a day. Build one list: the CRITICAL hosts
    #   in sorted order, followed by the OVERDUE hosts in sorted order.
    #   Print the first 3 under TODAY and whatever is left under TOMORROW, each
    #   host indented 3 spaces. Use slices. Do not write a loop that counts to 3.
    print("TODAY")
    print("TOMORROW")

    print()
    print("-" * 66)
    print("AUDIT FORECAST")
    print("-" * 66)
    entry = input("Days until the audit: ")
    while entry.isdigit() == False:
        print("  That is not a whole number.")
        entry = input("Days until the audit: ")

    # TODO 18
    #   entry is a string. Convert it, then use will_lapse to find every host that
    #   is COMPLIANT today and will not be on audit day. Print each of those host
    #   names indented 3 spaces, then the line below with the real count in place
    #   of the 0.
    lapsing = 0

    print(str(lapsing) + " compliant hosts will lapse before the audit.")

    print()
    print("-" * 66)
    print("HOST LOOKUP")
    print("-" * 66)
    print("Enter a host name, or 'done' to finish.")
    # TODO 19
    #   Keep asking with the prompt "Host: " until the user enters done.
    #   For a host in the inventory, find its position with HOSTS.index() and print
    #   its status, its days since patch and its days overdue on one line.
    #   For anything else print "  Not in the inventory."

    # TODO 20
    #   Three unknown host names in a row means the analyst is guessing, so the
    #   lookup closes. Count the unknown names in the loop above. On the 3rd one
    #   print "  Too many unknown hosts. Lookup closed." and stop asking.
    #   Run it with 4 bad names and count the prompts.

    print("=" * 66)
