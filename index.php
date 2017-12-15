<html>
<body>
<form action="." method="post">
	<input type="submit" name="team" value="Badgers" style="color: white; background-color: red"/>
	<input type="submit" name="team" value="Packers" style="color: yellow; background-color: green"/>
	<input type="submit" name="team" value="Brewers" style="color: yellow; background-color: blue"/>
	<input type="submit" name="team" value="Bucks" style="color: #5C378A; background-color: #00471B; font-weight: bold; text-shadow: -1px -1px #FFFFFF, 1px 1px #FFFFFF, 1px -1px #FFFFFF, -1px 1px #FFFFFF"/>
	<input type="submit" name="team" value="off" style="color: white; background-color: black"/>
</form>
<?php
if ($_POST["team"] != "") {
	exec("python /home/pi/web/lights/lights.py " . $_POST["team"]);
}
?>
</body>
</html>
