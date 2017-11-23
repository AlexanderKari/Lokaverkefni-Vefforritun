<!DOCTYPE html>
<html>
<head>
	<title>Bæta Notanda</title>
	<link rel="stylesheet" type="text/css" href="./static/styles.css">
</head>
<body>
		<br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br> 
	<form action="/skra" method="POST">
		<h2>Bæta við notanda</h2>
		<div>
                <label>
                Notendanafn
                <input type="text" name="notendanafn" placeholder="Notendanafn" required="">
                </label>
        </div>
        <br>
        <div>
                <label>
                Lykilorð
                <input type = "password" name="lykilord" placeholder="Lykilorð" required="">
                </label>
        </div>
                <br>
                <input type = "submit" name = "login" value = "Skrá" />
	</form>
</body>
</html>