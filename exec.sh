for number in {1..1000}
do
python3 jumper.py $number | nc shell.hsctf.com 10001
done
exit 0
