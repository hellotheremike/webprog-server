#!"C:\XAMPP\perl\bin\perl.exe"
$data_file="data.txt";

open(DAT, "<$data_file") || open(DAT, ">$data_file");
$var = <DAT>;
close(DAT);

if($var == 'NULL'){
	$var = 0;
}

open (DATA, ">$data_file");
print DATA $var + 1;
close(DATA);

$| = 1;
print "HTTP/1.0 200 OK", "\n"; 
print "Content-Type: multipart/x-mixed-replace;boundary=myboundary\n\n"; 
print "--myboundary\n"; 
while(1){
	print "Content-Type: text/plain\n\n";
	open(DAT, "<$data_file") || open(DAT, ">$data_file");
	$raw_data=<DAT>;
	close(DAT);
	print "This program is listening for new visors, run 144.cgi to se the effect.\n\n";
	print "Vistors: ";
	print $raw_data;
	sleep (1);
	print "\n--myboundary";
}