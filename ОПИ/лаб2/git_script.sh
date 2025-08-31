#!/bin/bash

# Initialize the repository
mkdir ~/git_lab2
cd ~/git_lab2
git init
echo "Initialized an empty Git repository."

# Configure user red
git config --local user.name "red"
git config --local user.email "red@itmo.niu"

# Create initial file and commit
touch file.txt
git add .
git commit -m "r0"
echo "Created file.txt and committed as r0"

# Create branch2 and switch to it
git checkout -b 'branch2'
echo "Switched to a new branch 'branch2'"

# Add content and commit as user blue
git config --local user.name "blue"
git config --local user.email "blue@itmo.niu"
echo -e "commit r1\n" >> file.txt
git add .
git commit -m 'r1'
echo "Added content and committed as r1 on branch2"

# Switch back to master and continue as user red
git checkout master
git config --local user.name "red"
git config --local user.email "red@itmo.niu"

# Add more commits on master
echo -e "commit r2\n" >> file.txt
git add .
git commit -m 'r2'
echo -e "commit r3\n" >> file.txt
git add .
git commit -m 'r3'
echo -e "commit r4\n" >> file.txt
git add .
git commit -m 'r4'
echo "Added commits r2, r3, and r4 on master"

# Switch to branch2 and add content as user blue
git checkout branch2
git config --local user.name "blue"
git config --local user.email "blue@itmo.niu"
echo -e "commit r5\n" >> file.txt
git add .
git commit -m 'r5'
echo "Added content and committed as r5 on branch2"

# Create branch3 and add commits as user red
git config --local user.name "red"
git config --local user.email "red@itmo.niu"
git checkout -b 'branch3'
echo -e "commit r6\n" >> file.txt
git add .
git commit -m 'r6'
echo -e "commit r7\n" >> file.txt
git add .
git commit -m 'r7'
echo "Added commits r6 and r7 on branch3"

# Switch to branch2 and add content as user blue
git checkout branch2
git config --local user.name "blue"
git config --local user.email "blue@itmo.niu"
echo -e "commit r8\n" >> file.txt
git add .
git commit -m 'r8'
echo "Added content and committed as r8 on branch2"

# Switch to branch3 and attempt to merge branch2
git checkout branch3
git config --local user.name "red"
git config --local user.email "red@itmo.niu"
git merge branch2
echo "Merge conflict! Please resolve manually and commit."

# Continue merge and add commit r9 on branch3
git add .
git merge --continue
echo -e "commit r9\n" >> file.txt
git add .
git commit -m 'r9'
echo "Resolved merge conflict and added commit r9 on branch3"

# Add commits r10 and r11 on branch3
echo -e "commit r10\n" >> file.txt
git add .
git commit -m 'r10'
echo -e "commit r11\n" >> file.txt
git add .
git commit -m 'r11'
echo "Added commits r10 and r11 on branch3"

# Switch to master and add commit r12
git checkout master
echo -e "commit r12\n" >> file.txt
git add .
git commit -m 'r12'
echo "Added commit r12 on master"

# Switch to branch3 and add commit r13
git checkout branch3
echo -e "commit r13\n" >> file.txt
git add .
git commit -m 'r13'
echo "Added commit r13 on branch3"

# Switch to master and attempt to merge branch3 (conflict)
git checkout master
git merge branch3
echo "Merge conflict! Please resolve manually and commit."

# Continue merge and add commit r14 on master
git add .
git merge --continue
echo -e "commit r14\n" >> file.txt
git add .
git commit -m 'r14'
echo "Resolved merge conflict and added commit r14 on master"

