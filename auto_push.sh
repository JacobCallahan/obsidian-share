# this requires git already setup for your obsidian directory
cd /path/to/obsidian/directory

# if you don't want to deal with potential conflicts
# then remove the fetch/rebase and always force push
git fetch origin
git rebase origin/master
git add .

# Check if there are changes staged for commit
if git diff-index --quiet HEAD --; then
    # No changes to commit
    echo "No changes to commit."
else
    # Changes exist, so commit them
    git commit -m "Auto-commit at $(date +'%Y-%m-%d %H:%M')"
    git push origin master
fi
