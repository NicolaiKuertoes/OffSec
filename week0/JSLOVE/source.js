var http = require('http');
const crypto = require('crypto');
var url = require('url');
var fs = require('fs');

var _0x777=["\xAF\xFE\x11","ff231231312312thisisnothex"];

function generatePw() {
    return
         {
             x: crypto[_0x777[1]](8)

         }[x].toString(_0x777[0]);
}

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    passwd = "passwd_" + generatePw();
    var url_content = url.parse(req.url, true);

    if (passwd == url_content.query.passwd) {
       res.write(fs.readFileSync('flag.txt', 'utf8'));
    } else {
        var source = fs.readFileSync(__filename, 'utf8');
        res.write('<html><body><form method="get"><input type="text" name="passwd" value="password"><input type="submit" value="login" /></form></div></body></html>');
    }
    res.end();
}).listen(8888);


console.log("passwd_" + generatePw());
