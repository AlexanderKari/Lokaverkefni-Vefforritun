<!DOCTYPE html>
<html>
<head>
        <title>Lokaverkefni</title>
        <link rel="stylesheet" type="text/css" href="./static/styles.css">
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
        <form action = "/login" method = "post">
        <h2>Upplýsingar</h2>
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
                <input type = "submit" name = "login" value = "Login" />

</body>
</html>