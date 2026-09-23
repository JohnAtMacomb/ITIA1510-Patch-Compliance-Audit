"""
Week 06 INDIVIDUAL ASSIGNMENT -- Patch Compliance Audit
ITIA 1510 Cybersecurity Automation

Topic: lists, from Week 05, and everything before them. if / elif / else,
for loops and functions. No dictionaries.

Every server and computer needs its security patches. This program checks how
long each one has gone without a patch, gives it a status, and reports how
much of the network follows the patch policy.

THE POLICY
   Criticality 3 (domain controllers, databases)   patch within 14 days
   Criticality 2 (servers)                          patch within 30 days
   Criticality 1 (workstations, kiosks)             patch within 60 days

   COMPLIANT   days since patch is the limit or less
   OVERDUE     past the limit, but no more than twice the limit
   CRITICAL    more than twice the limit
   EXEMPT      the host is on the exception list. Its numbers do not matter.

Work through the 10 numbered TODOs in order. Each one is a few lines. One
function is finished and wrong, and fixing it is part of the job.

Every function shows its types. In
   def patch_limit(criticality: int) -> int:
criticality is a whole number, and the function returns a whole number.
Python does not check the types. They are there for the person reading the
code. They need Python 3.9 or newer.

Run the file before changing anything. It works, but every answer is wrong,
because every function still returns a placeholder.

The host names are made up.
"""

# The inventory is three lists that line up. Position 0 in each list is the
# same host, position 1 is the next host, and so on.
HOSTS = [
    "dc-01", "dc-02", "web-01", "web-02", "db-01", "mail-01",
    "file-01", "hr-laptop-07", "kiosk-03", "lab-sandbox-01", "lab-sandbox-02",
]
DAYS_SINCE_PATCH = [9, 31, 12, 45, 95, 30, 61, 130, 58, 400, 200]
CRITICALITY = [3, 3, 2, 2, 3, 2, 1, 1, 1, 1, 1]

# Hosts on the exception list. They are left out of the compliance rate.
EXEMPT = ["lab-sandbox-01", "lab-sandbox-02"]

# The order the summary prints in.
STATUS_ORDER = ["COMPLIANT", "OVERDUE", "CRITICAL", "EXEMPT"]


# ---------------------------------------------------------------------------
# Part 1: one host at a time
# ---------------------------------------------------------------------------

def patch_limit(criticality: int) -> int:
    """Return the number of days the policy allows: 14, 30 or 60."""
    # TODO 1
    #   if / elif / else. Criticality 3 gets 14 days, criticality 2 gets 30,
    #   anything else gets 60.
    return 0


def patch_status(host: str, days: int, criticality: int, exempt: list[str]) -> str:
    """Return 'EXEMPT', 'COMPLIANT', 'OVERDUE' or 'CRITICAL'."""
    # TODO 2
    #   Check EXEMPT first: if host is in exempt, return "EXEMPT".
    #   Then get the limit from patch_limit(). The numbers 14, 30 and 60
    #   should not appear in this function.
    #      days is the limit or less          -> "COMPLIANT"
    #      days is twice the limit or less    -> "OVERDUE"
    #      anything else                      -> "CRITICAL"
    return "UNKNOWN"


def days_overdue(days: int, criticality: int) -> int:
    """Return how many days past the limit a host is, or 0 when it is not late."""
    # TODO 3
    #   Subtract the limit from days. If the answer is below 0, return 0.
    return 0


# ---------------------------------------------------------------------------
# Part 2: the whole inventory
# ---------------------------------------------------------------------------

def build_statuses(hosts: list[str], days: list[int], crits: list[int], exempt: list[str]) -> list[str]:
    """Return a new list with the status of every host, in the same order."""
    # TODO 4
    #   Start with an empty list. Loop over the positions with
    #      for i in range(len(hosts)):
    #   and use i to reach into all three lists. Append each status.
    return []


def count_status(statuses: list[str], wanted: str) -> int:
    """Return how many entries in statuses equal wanted."""
    # TODO 5
    #   Start a counter at 0 and loop. Do not use the .count() method.
    return 0


def hosts_with_status(hosts: list[str], statuses: list[str], wanted: str) -> list[str]:
    """Return a list of the host names whose status equals wanted."""
    # TODO 6
    #   hosts and statuses line up, the same way the inventory does. Loop over
    #   the positions and append hosts[i] when statuses[i] is wanted.
    return []


def average_days(days: list[int], statuses: list[str]) -> float:
    """Return the average days since patch, leaving out EXEMPT hosts,
    rounded to 1 decimal place."""
    # TODO 7 -- DEBUG
    #   This function is finished and it is wrong. The right answer is 52.3.
    #   It returns 57.8. Set a breakpoint on the for line, step through, and
    #   watch i. Find the host it never looks at, and fix the function.
    #   It cannot be tested until TODO 4 is done.
    if len(statuses) == 0:
        return 0.0
    total = 0
    count = 0
    for i in range(1, len(statuses)):
        if statuses[i] != "EXEMPT":
            total = total + days[i]
            count = count + 1
    return round(total / count, 1)


# ---------------------------------------------------------------------------
# Part 3: the report
# ---------------------------------------------------------------------------

# The report runs only when this file is run directly, so the test file can
# import the functions above without the report printing.
if __name__ == "__main__":
    statuses = build_statuses(HOSTS, DAYS_SINCE_PATCH, CRITICALITY, EXEMPT)

    print("=" * 56)
    print("PATCH COMPLIANCE AUDIT")
    print("=" * 56)
    print("Hosts in the inventory:   " + str(len(HOSTS)))
    print("Hosts that are audited:   " + str(len(HOSTS) - count_status(statuses, "EXEMPT")))

    print()
    print("HOST".ljust(16) + "CRIT".ljust(6) + "DAYS".ljust(7) + "STATUS".ljust(11) + "OVERDUE")
    print("-" * 56)
    # TODO 8
    #   Print one line for every host, lined up under the headings, using the
    #   same .ljust() widths. Numbers need str() first. The last column is
    #   days_overdue() for that host.

    print()
    print("SUMMARY")
    print("-" * 56)
    for status in STATUS_ORDER:
        print(status.ljust(12) + str(count_status(statuses, status)))

    # TODO 9
    #   The compliance rate is the COMPLIANT hosts as a percent of the hosts
    #   that are audited (every host that is not EXEMPT), rounded to 1 place.
    #   The verdict is PASS at 90 or more, AT RISK at 70 or more, FAIL below 70.
    rate = 0.0
    verdict = "UNKNOWN"

    print()
    print("Compliance rate:          " + str(rate) + "%")
    print("Audit verdict:            " + verdict)
    print("Average days since patch: " + str(average_days(DAYS_SINCE_PATCH, statuses)))

    print()
    print("ESCALATION QUEUE")
    print("-" * 56)
    # TODO 10
    #   Build one list named queue: the CRITICAL hosts in sorted order, then
    #   the OVERDUE hosts in sorted order. Use hosts_with_status(), sorted()
    #   and +. Print each host in queue on its own line, 3 spaces in.
    queue = []

    print("=" * 56)
