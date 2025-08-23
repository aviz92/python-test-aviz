#!/bin/bash
set -e

# usage: ./run_jira_check.sh JIRA_KEY [BRANCH]
JIRA_KEY="$1"
BRANCH="${2:-$(git rev-parse --abbrev-ref HEAD)}"
SHA=$(git rev-parse HEAD)

if [ -z "$JIRA_KEY" ]; then
  echo "Usage: $0 JIRA_KEY [BRANCH]"
  exit 1
fi

echo "Running Jira CI with:"
echo "  Jira key: $JIRA_KEY"
echo "  Branch:   $BRANCH"
echo "  SHA:      $SHA"

gh workflow run "Jira CI with PR Check" \
  --ref "$BRANCH" \
  -f jira_key="$JIRA_KEY" \
  -f sha="$SHA"
