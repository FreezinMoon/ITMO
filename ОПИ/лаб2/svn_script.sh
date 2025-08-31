#!/bin/bash
cd ~
export SVN_EDITOR=vim
mkdir -p $HOME/svnrepos/
svnadmin create $HOME/svnrepos/repo
svn mkdir file:///$HOME/svnrepos/repo/trunk file:///$HOME/svnrepos/repo/branches file:///$HOME/svnrepos/repo/tags -m "Create directory structure."

# r0: Initial commit on trunk
svn checkout file:///$HOME/svnrepos/repo/trunk work
cd work
cp ../data/commit0/* .
svn add *
svn commit -m "r0" --username=red

# Create branch2 from trunk at r0
svn copy file:///$HOME/svnrepos/repo/trunk file:///$HOME/svnrepos/repo/branches/branch2 -m "Creating branch2" --username=red

# r1: First commit on branch2
svn checkout file:///$HOME/svnrepos/repo/branches/branch2 branch2
cd branch2
cp ../../data/commit1/* .
svn commit -m "r1" --username=blue

# r2-r4: Commits on trunk
cd ..
for i in {2..4}
do
  cp ../data/commit$i/* .
  svn commit -m "r$i" --username=red
done

# r5: Second commit on branch2
cd branch2
cp ../../data/commit5/* .
svn commit -m "r5" --username=blue

# Create branch3 from branch2 at r5
svn copy file:///$HOME/svnrepos/repo/branches/branch2 file:///$HOME/svnrepos/repo/branches/branch3 -m "Creating branch3" --username=blue

# r6-r7: Commits on branch3
svn checkout file:///$HOME/svnrepos/repo/branches/branch3 branch3
cd branch3
for i in {6..7}
do
  cp ../../../data/commit$i/* .
  svn commit -m "r$i" --username=red
done

# r8: Third commit on branch2
cd ..
cp ../../data/commit8/* .
svn commit -m "r8" --username=blue

# Merge branch2 into branch3
cd branch3
svn update
svn merge file:///$HOME/svnrepos/repo/branches/branch2 --username=red
# Resolve conflicts if they occur and then commit
cp ../../data/commit9/* .
svn commit -m "r9" --username=red

# r10-r11: Additional commits on branch3
for i in {10..11}
do
  cp ../../../data/commit$i/* .
  svn commit -m "r$i" --username=red
done

# r12: Commit on trunk
cd ../..
cp ../data/commit12/* .
svn commit -m "r12" --username=red

# r13: Commit on branch2
cd branch2/branch3
cp ../../../data/commit13/* .
svn commit -m "r13" --username=red

# Merge branch3 into trunk to get r14
cd ../..
svn update
svn merge file:///$HOME/svnrepos/repo/branches/branch3 --username=red
# Resolve conflicts if they occur and then commit
cp ../data/commit14/* .
svn resolved *
svn commit -m "r14" --username=red

