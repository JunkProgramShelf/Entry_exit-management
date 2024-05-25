<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title></title>
</head>
<body>

<?php
$i=0;
const sq=50;#床面積[m^2](デフォルト),可変
$popu=0;
$j=0;
$data=0;
$type=$_POST["place"];
$num=array();
$fp=fopen('./meibo.csv','r');
if(! $fp){
	echo "OPEN ERROR<br>";
}
while($rowdata=fgetcsv($fp)){
	$num[$i]=$rowdata;
	#print_r($rowdata);echo"<br>";
	#echo$i;
	$i++;
}
//人数確認
for($i=1;$i<count($num);$i++){
	$data+=$num[$i][$type];
}
#人口密度確認
$popu=$data/sq;

echo "現在の利用人数:".$data."<br>";
echo"人口密度:".$popu;

fclose($fp);
?>

</body>
</html>
