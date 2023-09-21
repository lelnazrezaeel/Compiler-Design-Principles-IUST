
grammar Url;

url
   : scheme '://' host_str (':' port)? ('/' path?)? query? frag? WS? EOF
   ;

scheme
   : string
   ;

host_str
   : string ('.' string)*
   | '[' host_ip ']'?
   ;

host_ip
   : '::'? (string | DIGITS) ((':'|'::') (string | DIGITS))*
   ;

port
   : DIGITS
   ;

path
   : string ('/' string)* '/'?
   ;

frag
   : '#' (string | DIGITS)
   ;

query
   : '?' search
   ;

search
   : searchparameter ('&' searchparameter)*
   ;

searchparameter
   : string ('=' (string | DIGITS | HEX))?
   ;

string
   : STRING
   | DIGITS
   ;


DIGITS
   : [0-9] +
   ;


HEX
   : ('%' [a-fA-F0-9] [a-fA-F0-9]) +
   ;


STRING
   : ([a-zA-Z~0-9] | HEX) ([a-zA-Z0-9.+-] | HEX)*
   ;


WS
   : [\r\n] +
   ;