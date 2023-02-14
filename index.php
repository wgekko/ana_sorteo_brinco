<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ana Loteria</title>
    <link rel="stylesheet" type="text/css" href="./estilos/estilos.css">
    <link rel="stylesheet" type="text/css" href="./estilos/style.css">
    <!--<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css">-->
</head>
<body>
     <header id="header">
      <a href="" target="_blank"><img src="/img/android-chrome-225x225.png" class="logo" alt="logo__Ana" id="header_logo"></a>
      <h1>Ana - Brinco/Quini6 TechSystem - </h1>
      <br><br>
      <div class="botones">
          <button type="button" class="menu" onclick="window.location.href = '#';">Volver al Menu</button>
          <button type="button" class="salida" onclick="window.location.href = '#';">Salir</button>
      </div>
    </header>
     <main>
        <h1>Brinco</h1>
        <form method="post">
          <label for= "numbers" >Digite los 6 números :</label>
          <input type="number" id="number1" name="number1" size="4" required="">
          <input type="number" id="number2" name="number2" size="4" required="">
          <input type="number" id="number3" name="number3" size="4" required="">
          <input type="number" id="number4" name="number4" size="4" required="">
          <input type="number" id="number5" name="number5" size="4" required="">
          <input type="number" id="number6" name="number6" size="4" required="">
          <button type="submit">Ver aciertos</button>
        </form>
     </main>
     <footer>
    <div class="redes">
      <span class="copyrigth">&#169; Walter Gomez - 2023</span>
      <a href="https://github.com/login" target="_blank"><img class="imgRedes" src="./img/Github.png" alt="Github"></a>
      <a href="https://ar.linkedin.com/" target="_blank"><img class="imgRedes" src="./img/Linkedin.png" alt="Linkedin"></a>
      <a href="mailto:waltergomez75@gmail.com" target="_blank"><img class="imgRedes" src="./img/gmail.png" alt="Gmail"></a>
     </div>
    </footer>
</body>
</html>

