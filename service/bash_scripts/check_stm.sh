FILE=/media/<user>/NODE_F446RE
if [ -d "$FILE" ]; then
    echo "$FILE is a directory."
    exit 0
else
    echo "$FILE is not a directory."
    exit 1
fi
