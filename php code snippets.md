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



    
