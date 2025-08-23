# Python Test Package

## Run Jira Check
1. **Positional style**
   ```bash
   ./run_jira_check.sh ABC-123
   ./run_jira_check.sh ABC-123 feature/some-branch
   ```
2. **Key=Value style**

   ```bash
   ./run_jira_check.sh JIRA_KEY=ABC-123
   ./run_jira_check.sh JIRA_KEY=ABC-123 BRANCH=feature/some-branch
   ```

And in all cases:

* If `BRANCH` isn’t provided → it auto-detects from `git rev-parse --abbrev-ref HEAD`.
* `SHA` is always taken as the **latest commit** on that branch (`git rev-parse HEAD`), unless you explicitly pass `SHA=...`.

<br>

---

## Pytest by Marker
1. **Run pytest with marker "slow" on current branch**
    ```bash
    ./run_pytest_marker.sh dummy
    ```

2. **Run pytest with marker "integration" on a specific branch**
    ```bash
   ./run_pytest_marker.sh integration feature/some-branch
    ```
