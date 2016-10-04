curl -v $1 2>&1 | grep 'Location'| cut -d' ' -f3
