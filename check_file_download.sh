#creating function
_func() {

x=`du -sk "$FILEPATH" | awk '{ print $1 }'`
sleep 5
y=2

while [ "$x" != "$y" ]
do
y=`du -sk "$FILEPATH" | awk '{ print $1 }'`
echo "size before sleep is $y"
echo "sleep for another 60 seconds"
sleep 60
x=`du -sk "$FILEPATH" | awk '{ print $1 }'`
echo "size after sleep $x"
done

}

#using function
if _func ; then
echo "downloading is complete"
else
echo "downloading"
fi
