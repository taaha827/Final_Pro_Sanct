<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <table>

        <tr>
            <td><h2>Image Data</h2></td>
            <td><h2>Image</h2></td>
        </tr>

        <?php
        
        $con = mysqli_connect('localhost', 'root', '', 'daraz');

        $query = 'select * from daraz_data';

        $res = mysqli_query($con, $query);


        while($row = mysqli_fetch_assoc($res)){
        ?>
         <tr>
            <td><?= $row['TextRead']?></td>
            <td><img src="<?= $row['FilePath']?>" /></td>
        </tr>

        <?php } ?>

    </table>
    
</body>
</html>