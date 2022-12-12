### Get Records 

```php

<?php
$sql = "SELECT * FROM brothers_q";

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        //Code-Here
    }
}

?>

            

```
