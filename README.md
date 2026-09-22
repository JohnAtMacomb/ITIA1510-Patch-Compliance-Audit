# ITIA 1510 Week 06: Patch Compliance Audit

Individual assignment. Topic: **lists**, from Week 05, and everything before
them.

Your program reads the patch inventory, gives every host a status against the
patch policy, and reports how much of the network is inside that policy. Open `patch_audit.py` and work through the 20 numbered TODOs in
order. Two of the functions are finished and wrong, and fixing them is part of
the job. No dictionaries.

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

| Question                                  | Answer                             |
|-------------------------------------------|------------------------------------|
| Hosts that are audited                    | 11                                 |
| Compliant                                 | 4                                  |
| Overdue                                   | 2                                  |
| Critical                                  | 3                                  |
| Exempt                                    | 2                                  |
| Invalid                                   | 2                                  |
| Compliance rate                           | 44.4%                              |
| Audit verdict                             | FAIL                               |
| Average days since patch                  | 52.3                               |
| Most overdue host                         | db-01, 81 days past its limit      |
| Escalation queue, today                   | db-01, dc-02, hr-laptop-07         |
| Escalation queue, tomorrow                | file-01, web-02                    |

Entering `10` at the forecast prompt lists `dc-01`, `mail-01` and `kiosk-03`,
and reports that 3 compliant hosts will lapse before the audit.

Four unknown host names in a row at the lookup prompt produce three prompts,
not four.
