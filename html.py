#Connection website
index = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

<center><h1>Connect your light</h1></center>

<center><form action="/connect" method="post">
  <label for="ssid">SSID:</label><br>
  <input type="text" id="fname" name="fname" value=""><br>
  <label for="pass">PASS:</label><br>
  <input type="text" id="lname" name="lname" value=""><br><br>
  <input type="submit" value="Submit">
</form></center> 


</body>
</html>
"""

con =  """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

<center><h1>Connect your milkie</h1></center>

<center><h3>Connecting...<h3></center> 


</body>
</html>
"""

succ =  """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

<center><h2 style="color:#008000">Conected!</h2></center>
 


</body>
</html>
"""
