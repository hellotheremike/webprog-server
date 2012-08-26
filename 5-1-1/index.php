<html>
<body>

<?php
if (isset($_REQUEST['to']) && $_REQUEST['password'] == '1234'){
  $to = $_REQUEST['to'];
  $subject = $_REQUEST['subject'];
  $message = $_REQUEST['message'];
  $headers = "From: ". $_REQUEST['from'] . 
       "\r\n" ."CC: " . $_REQUEST['cc'] .
       "\r\n" ."BCC: " . $_REQUEST['bcc'];

  mail($to,$subject,$message,$headers);
  echo "<div>
  <h1>Mail Sent!</h1>
  To: {$to}<br />
  From: {$_REQUEST['from']}<br />
  Cc: {$_REQUEST['cc']}<br />
  Bcc: {$_REQUEST['bcc']}<br />
  Subject: {$_REQUEST['subject']}<br />
  Message:
  <br />
  {$_REQUEST['message']}
  <br />
  Password: {$_REQUEST['password']}
  </div>";
}
else{
  echo "<form method='post' action=''>
  To: <input name='to' type='text' /><br />
  From: <input name='from' type='text' /><br />
  Cc: <input name='cc' type='text' /><br />
  Bcc: <input name='bcc' type='text' /><br />
  Subject: <input name='subject' type='text' /><br />
  Message:<br />
  <textarea name='message' rows='15' cols='40'>
  </textarea><br />
  <input type='password' name='password'/>
  <input type='submit' />
  </form>";
  }
?>

</body>
</html>