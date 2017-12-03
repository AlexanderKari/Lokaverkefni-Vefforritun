<h1>Cool myndasíða</h1>
<link rel="stylesheet" type="text/css" href="./static/style3.css">
<body>
% for i in range(0,len(gogn['myndir'])):
	<h3>Drift og bílahittingar</h3>
	<h4>Mynd heiti: {{ gogn['myndir'][i]['mynd'] }}</h4>
	<img src="./myndir/{{gogn['myndir'][i]['mynd']}}"><br>
% end
<a href="/" title="Til baka" id="arrow">&#x21E7;</a>
</body>