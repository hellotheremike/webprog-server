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
print "Content-Type: text/plain\n\n";
print "Vistors: ";
print $var + 1;
