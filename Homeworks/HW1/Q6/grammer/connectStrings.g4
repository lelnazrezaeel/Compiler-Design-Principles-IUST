grammar connectStrings;

start :
    '"' connect_strings'"' EOF
    ;

connect_strings :
    (server | security | catalog) (';'? connect_strings)*
    ;

server :
    (Se_keyword '=' Se_description );
    Se_keyword : 'server' ;
    Se_description : '(localdb)' | '(local)' ;

security :
    (S_keyword '=' S_description );
    S_keyword : 'Persist Security Info' | 'Integrated Security' ;
    S_description : 'true' | 'True' | 'yes' | 'false' | 'False' | 'no' ;

catalog :
    (C_keyword '=' C_description );
    C_keyword : 'Initial Catalog';
    C_description : STRING ;

STRING : [a-zA-Z~0-9]+;


