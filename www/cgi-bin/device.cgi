#!/bin/sh
echo "Content-Type: text/plain"
echo "Cache-Control: no-cache, must-revalidate"
echo "Expires: Sat, 26 Jul 1997 05:00:00 GMT"
echo

DEVICENAME="`cat /www/cgi-bin/device.txt | cut -f1 -d:`"
DEVICEIP="`cat /www/cgi-bin/device.txt | cut -f2 -d:`"

case "$QUERY_STRING" in
 "name")
 echo $DEVICENAME
 ;;
 "ipaddress")
 echo $DEVICEIP
 ;;
esac

