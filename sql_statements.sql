//Creating criminal database

create table criminals(id int,name varchar(20),age int,crime varchar(20),
photo1 longblob,photo2 longblob,photo3 longblob,ts timestamp default current_timestamp)


//Creating derived database

create table derived(id int,all_photos longblob,centroid_encoding longblob)

//Creating complaint database

create table complaint(identified_id int,ts timestamp default current_timestamp,location varchar(20),crime varchar(20),photo_uploaded longblob)
