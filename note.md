User
    uid
    ip

Tweets  
    tid         -   int, auto_increment, primary key(tid)
    uid         -   int
    post        -   varchar(140)
    date        -   datetime
    
Follows
    uid         -   int
    follower    -   primary key(uid, follower)