<html>
<head>
<title>Panel de control</title>
<meta http-equiv= "content-Type" content= "text/html; charset=UTF-8"/>
<link href="enquesta.css" rel="stylesheet"/>
<link rel="shortcut icon" href="./images/meteo.jpg">
	<link rel="stylesheet" href="css/normalize.css">
	<link rel="stylesheet" href="css/stylep.css">
</head>
<body >
	<div class="demo-wrapper css3-bounce-effect">
		<div class="css3-notification">
			<p>Edita aqui tus preferencias</p>
		</div>
	</div>
<div class="background" >

<h1 class="inset">Meteopy</h1>

<?
$con = mysql_connect("localhost", "root", "smx");
mysql_select_db("meteopy",$con);

$consulta1 = "select * from login where ID=1";	
$query = mysql_query($consulta1, $con);

if($row = mysql_fetch_array($query)){
?>
<form method="POST" action="procesar.phtml" >
<b>Tiempo:</b> <input type="text" name="tiempo" autofocus required value="<?=$row['user']?>"><br>
<b>Correo:</b> <input type="text" name="correo" required value="<?=$row['pass']?>"><br>
<input type="submit" value="Enviar">
</form>
<br>
Boto per iniciar el script de recollida de dades
<form action="start.php" method="get">
  <input type="submit" value="Inicialitzar els sensors ara!">
</form>
<br>
boto per apagar el sistema de forma segura
<form action="apagar.php" method="get">
  <input type="submit" value="Apagar el sistema ara!">
</form>


<?}?>
</div>
</body>
</html>