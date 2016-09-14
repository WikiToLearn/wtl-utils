#!/bin/bash

#enter actual directory of the script
cd "$(dirname "$0")"

cd pages

for file in *; do
    echo "$file"
    url=$(cat "$file" | curl -sF 'sprunge=<-' http://sprunge.us)    
    echo -e "$url"
    echo -e "wget $url -O \"$file\"; php moveBatch.php \"$file\"" 
    echo -e "\n"
done
