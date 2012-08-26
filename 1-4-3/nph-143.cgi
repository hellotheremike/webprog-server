#!"C:\XAMPP\perl\bin\perl.exe"
use File::Copy;
$| = 1;
print "HTTP/1.0 200 OK", "\n"; 
print "Content-Type: multipart/x-mixed-replace;boundary=myboundary\n\n"; 
print "--myboundary\n"; 
$tracker = 0;
$content = "";
for ($countdown = 10; $countdown > 0; $countdown--) {
	$tracker++;

	if ($tracker==1) {
		$content = "\n<br>countdown: $countdown";
		print "Content-Type: text/html\n\n";
		sleep (1);
	}
	elsif ($tracker==2) {
		$content = "\ncountdown: $countdown";
		print "Content-Type: text/plain\n\n";
		sleep (1);
	}
	elsif ($tracker==3) {
		$tracker = 0;
		print "Content-type: image/jpeg\n\n";
		copy "cam.gif", \*STDOUT;
		$content = "\ncountdown: $countdown";
		print "Content-Type: text/plain\n\n";
		sleep (1);
	}
	
	$time = gmtime( time());
	print $time;
	print "$content";
	print "\n--myboundary";
	

} 