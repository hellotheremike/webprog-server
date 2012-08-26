#!"C:\XAMPP\perl\bin\perl.exe"

$| = 1;
print "HTTP/1.0 200 OK", "\n"; 
print "Content-Type: multipart/x-mixed-replace;boundary=myboundary\n\n"; 
print "--myboundary\n"; 

for ($countdown = 10; $countdown > 0; $countdown--) {
	print "Content-Type: text/plain\n\n";
	print "\n";
	$time = gmtime( time());
	print $time;
	print "\n";
	print $countdown, "\n"; 
	sleep (1); 
	print "\n--myboundary";

} 