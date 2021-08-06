<?php

session_start();

$con=mysqli_connect('localhost','root');

mysqli_select_db($con,'sample');

$username = $_POST["name"];
$pass = $_POST["psw"];

$sql = "select Name from registration_demo where Name = '$username'";
$res = $con->query($sql);

if($res->num_rows==0)
{
echo "Invalid user";
}
else{

$sql = "select Password from registration_demo where Name = '$username'";
$res = $con->query($sql);
$row = $res->fetch_assoc();
if($row["Password"] != $pass)
echo"Invalid Credentials";
else
echo"Login succeeded";
}
?>
