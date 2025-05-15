#!/bin/bash

# --- Configuration ---
# The GitHub username or organization that owns the repository
REPO_OWNER="BitflipFTC"
# The name of the repository
REPO_NAME="website"
# The filename containing the PAT
TOKEN_FILE="gitkey.key"
# The username to associate with the commits made by this script
# This can be your actual GitHub username or a bot-like name
COMMIT_USER_NAME="BitflipFTC-Bot" # Or your GitHub username
# The email to associate with the commits
COMMIT_USER_EMAIL="bot@users.noreply.github.com" # Or your GitHub email

# --- Script Logic ---

# Function to exit with an error message
error_exit() {
  echo "ERROR: $1" >&2
  exit 1
}

# 1. Check if gitkey.key exists and read the token
if [ ! -f "$TOKEN_FILE" ]; then
  error_exit "Token file '$TOKEN_FILE' not found. Please create it and place your GitHub PAT inside."
fi

GITHUB_TOKEN=$(cat "$TOKEN_FILE")
if [ -z "$GITHUB_TOKEN" ]; then
  error_exit "Token file '$TOKEN_FILE' is empty or token could not be read."
fi

echo "Successfully read token from $TOKEN_FILE."

# 2. Configure Git user for this specific operation
# This overrides local Git config only for the commands run after this in the script.
echo "Configuring git user as '$COMMIT_USER_NAME <$COMMIT_USER_EMAIL>' for this operation..."
git config user.name "$COMMIT_USER_NAME"
git config user.email "$COMMIT_USER_EMAIL"

# 3. Add all changes in the current directory
echo "Adding all changes to staging area..."
git add . ':(exclude)*.key'

# 4. Commit the changes
# Check if there are any changes to commit
if git diff --staged --quiet; then
  echo "No changes to commit."
  exit 0
fi

COMMIT_MESSAGE="Automated update via script $(date)"
echo "Committing changes with message: '$COMMIT_MESSAGE'..."
git commit -m "$COMMIT_MESSAGE"

# 5. Construct the authenticated remote URL
# Using x-access-token is the recommended way for PATs
REMOTE_URL="https://x-access-token:${GITHUB_TOKEN}@github.com/${REPO_OWNER}/${REPO_NAME}.git"

# 6. Get the current branch name
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ -z "$CURRENT_BRANCH" ]; then
    error_exit "Could not determine current branch."
fi
echo "Current branch is: $CURRENT_BRANCH"

# 7. Push to the repository
echo "Pushing changes to remote branch '$CURRENT_BRANCH'..."
git -c credential.helper= push "${REMOTE_URL}" "HEAD:${CURRENT_BRANCH}"

if [ $? -eq 0 ]; then
  echo "Push successful to ${REPO_OWNER}/${REPO_NAME} on branch ${CURRENT_BRANCH}."
else
  # Optional: Revert local commit if push fails and you want a clean state
  # echo "Push failed. Reverting local commit."
  # git reset --hard HEAD~1
  error_exit "Push failed. Check token permissions, remote URL, and network."
fi

echo "Script finished successfully."