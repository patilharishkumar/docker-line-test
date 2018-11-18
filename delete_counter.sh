declare -a arr=$(curl -s http://127.0.0.1/counter/|python -c "import sys, json; print json.load(sys.stdin)['result']" | tr -d '[],'|tr -d "u',");
## now loop through the above array
for i in $arr;
do
   #echo "$i"
   curl -X POST http://127.0.0.1/counter/${i}/stop
done
