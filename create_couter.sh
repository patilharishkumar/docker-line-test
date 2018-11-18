for ((i=1;i<=$1;i++))
do
curl  -d "to=100" -X POST http://127.0.0.1/counter/
done
