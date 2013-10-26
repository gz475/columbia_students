cat 2012_12_15.txt | cut -f6 -d' ' | tail -n +2 | sort -n -r | head -n 1 

echo 'done'

cat 2012_12_15.txt | cut -f1 -d' '
