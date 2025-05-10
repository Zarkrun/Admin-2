<?php
$dbname = getenv('MARIADB_DATABASE');
$dbhost = getenv('MARIADB_HOST');
$dbuser = getenv('MARIADB_USER');
$dbpass = getenv('MARIADB_PASSWORD');

$conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);

if ($conn->connect_error) {
	die("Echec de connexion : " . $conn->connect_error);
} else {
	echo "Connexion réussie à la base de données !";
}

$conn->close();
?>
