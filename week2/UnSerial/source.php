<?php
include("db_driver.php");


class ShellCommand {
   function is_ok($cmd) {
           return false;  // disabled for now
   }
   function __construct($cmd) {
      if ($this->is_ok($cmd)) {
         $this->cmd = $cmd; 
      }
   }
   function exec() {
       system($this->cmd);
   } 
}


class DB {
    function __construct() {
        $this->db_driver = new DBDriver();
    }
    function exec($query) {
        return $this->db_driver->do_query($query);
    }
}


class User {
    function __construct($uid, $name) {
            $this->uid = $uid;
            $this->name = $name;
            $this->db = new DB();
            $this->active = true;
    }
    function __wakeup() {
        if ($this->db->exec("SELECT * FROM SESSIONS WHERE uid=". $this->uid)) { // session still active
            $this->active = true;
        } else {
            $this->active = false;
        }
    }
}


if (isset($_COOKIE['session'])) {
    $user = unserialize($_COOKIE['session']);
    echo "You are logged in as " . $user->name;
} else {
    $cookie = new User(1234, "guest");
    setcookie('session', serialize($cookie));
    header("Location: /");
}
