<?php
// PHP Data Objects(PDO) Sample Code:
try {
    $conn = new PDO("sqlsrv:server = tcp:operatingsystems.database.windows.net,1433; Database = student_records", "CloudSA8834b57b", "{your_password_here}");
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
}
catch (PDOException $e) {
    print("Error connecting to SQL Server.");
    die(print_r($e));
}

// SQL Server Extension Sample Code:
$connectionInfo = array("UID" => "CloudSA8834b57b", "pwd" => "{your_password_here}", "Database" => "student_records", "LoginTimeout" => 30, "Encrypt" => 1, "TrustServerCertificate" => 0);
$serverName = "tcp:operatingsystems.database.windows.net,1433";
$conn = sqlsrv_connect($serverName, $connectionInfo);
?>
