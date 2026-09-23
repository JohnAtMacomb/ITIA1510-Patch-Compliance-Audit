# ITIA 1510 Week 06: Patch Compliance Audit

Individual assignment. Topic: **lists**, from Week 05, and everything before
them. No dictionaries.

Every server and computer needs its security patches. Your program checks how
long each one has gone without a patch, gives it a status, and reports how
much of the network follows the patch policy.

Open `patch_audit.py` and work through the 10 numbered TODOs in order. Each
one is a few lines. One function is finished and wrong, and fixing it is part
of the job.

Every function has type hints, such as `list[str]` and `-> int`. They need
Python 3.9 or newer. Check with `python --version`.

## The policy

| Criticality | Hosts                          | Patch within |
|-------------|--------------------------------|--------------|
| 3           | domain controllers, databases  | 14 days      |
| 2           | servers                        | 30 days      |
| 1           | workstations, kiosks           | 60 days      |

A host is **COMPLIANT** at its limit or less, **OVERDUE** past the limit but
no more than twice it, and **CRITICAL** beyond that. A host on the exception
list is **EXEMPT**, whatever its numbers say.

## Get your own copy

1. On this repository's GitHub page, click **Use this template**, then
   **Create a new repository**.
2. Set **Owner** to your own account and name the repository
   `ITIA1510-Patch-Compliance-Audit`. Choose **Public**, then click
   **Create repository**.
3. Clone your new repository, not this one:

   ```
   git clone <your repository url>
   cd ITIA1510-Patch-Compliance-Audit
   ```

## Do the work on a branch

Do all of the git work with git commands from the command line. Do not edit,
upload or merge files in the GitHub web interface.

4. Create the branch before you change anything:

   ```
   git checkout -b week06-patch-compliance-audit
   ```

5. Write the code. Commit as you go:

   ```
   git add patch_audit.py
   git commit -m "Describe what you just finished"
   ```

6. Push the branch:

   ```
   git push -u origin week06-patch-compliance-audit
   ```

## Demonstrate, then merge

7. **Demonstrate the program to your instructor** from the branch you just
   pushed, using the debugger in VS Code. The demonstration is required: it is
   worth half the grade, and an assignment that is never demonstrated earns no
   points.
8. After the demonstration, merge into main and push:

   ```
   git checkout main
   git merge week06-patch-compliance-audit
   git push origin main
   ```

9. Submit the link to your repository in Canvas.

If it is not finished at 8:55 PM, keep working, or demonstrate what you have,
then commit, push, merge and submit it for partial credit.

## Check your work

With the data in `patch_audit.py`, a finished program gives these answers.

| Question                     | Answer                                        |
|------------------------------|-----------------------------------------------|
| Hosts that are audited       | 9                                             |
| Compliant, overdue, critical | 4, 2, 3                                       |
| Exempt                       | 2                                             |
| Compliance rate              | 44.4%                                         |
| Audit verdict                | FAIL                                          |
| Average days since patch     | 52.3                                          |
| Escalation queue             | db-01, dc-02, hr-laptop-07, file-01, web-02   |

The tests in `test_patch_audit.py` cover TODO 1 through TODO 7. Run them from
this folder:

```
python -m unittest test_patch_audit -v
```

19 of the 23 fail before you start, and all 23 pass when those functions are
right. The report TODOs, 8 through 10, are checked against the table above.
