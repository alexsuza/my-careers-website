#!/bin/bash

## stage files for commit
git add .

## commit new files
commit_message="$1"
git commit -m "$commit_message"
#
## push to GitHub
git push origin main


if git push origin main; then
	    echo "Push successful!"
    else
	        echo "Push failed!"
fi
