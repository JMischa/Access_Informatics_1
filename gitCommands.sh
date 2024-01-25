# git init
mkdir project-folder
cd project-folder
git init -q
git status
ls -la # show git directory

# git commit
echo "Hello World" >> hello.py
git status # show untracked files
git add . # add file to staging
git status # show staged files
git commit -am "first commit"
git status # files committed

# gitignore
echo "temp file" >> temp.tmp
git status # file is untracked
echo "*.tmp" >> .gitignore
git add .gitignore
git status # show that .tmp file is excluded
git commit -am "ignore added"

# git revert
git status
echo "some mistake" >> mistake.py
git add . && git commit -am "mistake committed"
echo "Now we revert"
git revert <commitHash>
ls -l # file was removed

# git branch
git branch # show current branches
git checkout -b newBranch main # create new branch from main

echo "branch" >> branch.py
git add branch.py && git commit -am "New file on branch"
ls # file is available
git checkout main # switch to the main branch
ls # file is not on the main branch

# git merge & git rebase
git log # show the current structure with branches
git branch
git merge newBranch main
git log # show merged commits

git reset --hard <commitBeforeMerge>
git log # show the state before merge again
git rebase newBranch
git log # show the state after using rebase

# orphan branch
git log # show commit history
git checkout --orphan orphanBranch
git status # show staged files
git commit -am "new root commit"
git log # show new commit history

# bisect
git log # show current log and see which commits are potentially bad

git bisect start
git bisect good <goodCommitId>
git bisect bad <badCommitId>

# checks out the midpoint between these two, and now we can run the tests again
# depending on the results, we continue.
# This results in a binary search through the commits in between these two

# tag and squash
git tag -n # shows all existing tags
git tag -a V1.2.1 -m "before squash" # adds a new tag
git log --decorate --oneline # show log with tags
git rebase -i main~3 # squash the last 3 commits interactively
# edit two of the commits to be squashed instead of picked
# pick -> squash
# add a new commit message for the combined commit

git log --decorate --oneline # show changes
git tag -a V1.2.2 -m "after squash"
git tag -n # show all tags
git checkout -b version1.2.2 V1.2.2 # create a new branch from the tag
