### Get Records 

```php

<?php
$sql = "SELECT * FROM table1";

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        //Code-Here
    }
}

?>

            

```


### Make Query After the results of another query


```php

<?php
$sql = "SELECT * FROM table1";

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $sql2 ="SELECT * FROM users where id=$sid";        
        $result2= $conn->query($sql2);
        $fullname=$result2->fetch_assoc();
        $fn=$fullname['firstname'];
        $ln=$fullname['lastname'];
        
        echo $fn.' '.$ln;
    }
}

?>

            

```


### Insert Data

```php
<?php

if (isset($_POST["msg"]) && !empty($_POST["msg"])) {
    $msg = mysqli_real_escape_string($conn, $_POST["msg"]);
    $rcvr = mysqli_real_escape_string($conn, $_GET["id"]);

    $q = "INSERT INTO chat(sndr,rcvr,msg,date) VALUES($sndr,$rcvr,'$msg','$date')";
    $result = $conn->query($q);
}

?>

```


    
