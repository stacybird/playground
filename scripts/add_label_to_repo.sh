#!/bin/bash
# Adds a label to the given repo 
# The environment variables GITUSER and GITPASS must be set correctly
# Minimal error checking.
# Kept simple so that this can be used in a loop for multiple tags or repos.
# Note if the tag already exists, github does a no-op (already_exists).  

if [ $# -ne 2 ]; then
    echo usage: $0 label_name repo_name
    echo eg: $0 approve_this myorg/myrepo
    exit
fi

STR=`which curl`
if [ "$STR" == "" ]; then
    echo "Sorry, curl needs to be installed first"
    exit
fi

DATA='{"name":"'$1'","color":"009800"}'

echo "attempting to add: "$DATA
curl --user "$GITUSER:$GITPASS" --include --request POST --data $DATA \
 "https://api.github.com/repos/$2/labels"

