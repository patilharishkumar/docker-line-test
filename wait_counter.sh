echo "Waiting for all Counters expire"
while true
do
declare -a arr=$(curl -s http://127.0.0.1/counter/|python -c "import sys, json; print json.load(sys.stdin)['result']" | tr -d '[],'|tr -d "u',");
## now loop through the above array
if [ -z "$arr" ]; then
   echo " All Counters Expired."
    break
fi
sleep 1
done
