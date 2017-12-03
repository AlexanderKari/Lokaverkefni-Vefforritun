<!DOCTYPE html>
<html>
<head>
	<title>Breyta lykilorði</title>
	<link rel="stylesheet" type="text/css" href="./static/style4.css">
        <link href="https://fonts.googleapis.com/css?family=Barlow" rel="stylesheet">
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
	<form action="/breyt" method="POST">
		<h2>Breyta lykilorði</h2>
        <div>
                <label>
                Lykilorð
                <input type = "password" name="lykilord" placeholder="Lykilorð" required="">
                </label>
        </div>
                <br>
                <input type = "submit" name = "login" value = "Skrá" />
	</form>
        <a href="/" title="Til baka" id="arrow">&#x21E7;</a>
</body>
</html>