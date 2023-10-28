<?php
$servername="mysql";
$username="root";
$password="mysecretpassword";
$dbname="mydb";
//Create Conexion
$conn=new mysqli($servername,$username,$password,$dbname);

if ($conn->connect_error) {
    die("Conexion Fallada" .$conn->connect_error);
}
echo "Connecion correcta a MYSQL";
$conn->close();
?>