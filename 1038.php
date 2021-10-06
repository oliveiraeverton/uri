<?php

$valores = readline();
$valoresFormatados = explode(' ', $valores);

$valor1 = $valoresFormatados[0];
$valor2 = $valoresFormatados[1];

if($valor1 == 1){
    echo "Total: R$ ", number_format(4.00*$valor2, 2, '.','').PHP_EOL;

}
else if($valor1 == 2){
    echo "Total: R$ ", number_format(4.50*$valor2, 2, '.','').PHP_EOL;

}
else if($valor1 == 3){
    echo "Total: R$ ", number_format(5.00*$valor2, 2, '.','').PHP_EOL;

}
else if($valor1 == 4){
    echo "Total: R$ ", number_format(2.00*$valor2, 2, '.','').PHP_EOL;

}
else{
    echo "Total: R$ ", number_format(1.50*$valor2, 2, '.','').PHP_EOL;

}

?>
