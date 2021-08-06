<?php

session_start();
$con = mysqli_connect('localhost','root');

mysqli_select_db($con, 'sample');

$name = $_POST["name"];
$pass = $_POST["psw"];
$email = $_POST["email"];
$phone = $_POST["phn"];

$s = "select * from registration_demo where Name = '$name'";

$result = mysqli_query($con,$s);

$num = mysqli_num_rows($result);

if($num==1)
{
echo "Username already taken";
}
else{
$reg="insert into registration_demo(Name,Email,Password,Phone) values('$name','$email','$pass','$phone')";
mysqli_query($con,$reg);
echo"Registration Successful";
}


?>
