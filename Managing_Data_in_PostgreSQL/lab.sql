create table dog_room(
    room_id int primary key not null,
    dog_id int not null,
    hotel_id int not null,
    register_date date,
    unregister_date date
) 
---------------------------------
create table cat_room(
    room_id int primary key not null,
    cat_id int not null,
    hotel_id int not null,
    register_date date,
    unregister_date date
) 
--------------------------------------
create table dog(
    dog_id int primary key not null,
    owner_id int not null,
    dog_name varchar(15),
    dog_age integer not null,
    check (
        dog_age between 1
        and 25
    )
) 
-------------------------------------
create table cat(
    dog_id int primary key not null unique,
    owner_id int not null,
    cat_name varchar(15),
    cat_age integer not null,
    check (
        cat_age between 1
        and 25
    )
) 
-----------------------------------
create table hotel (
    hotel_id int primary key unique not null,
    hotel_name varchar(25),
    hotel_stars int,
    check (
        hotel_stars between 1
        and 5
    )
)
-----------------------------------
create table pet_owner(
    owner_id int primary key not null unique,
    owner_name varchar(15),
    owner_age int not null,
    check (
        owner_age between 1
        and 100
    )
)
----------------------------------
INSERT INTO
    pet_owner(owner_id, owner_name, owner_age)
VALUES
    (1, 'Peter', 26),
    (2, 'George', 32),
    (3, 'Amy', 67)
------------------------
INSERT INTO
    dog(dog_id, owner_id, dog_name, dog_age)
values
    (1, 1, 'Fluffy', 2),
    (2, 3, 'Bully', 3),
    (3, 1, 'Rousey', 5)
-----------------
INSERT INTO
    cat(cat_id, owner_id, cat_name, cat_age)
values
    (1, 2, 'Tommy', 1),
    (2, 3, 'Jessy', 7),
    (3, 1, 'Bubbles', 3)
------------------------
INSERT INTO
    hotel(hotel_id, hotel_name, hotel_stars)
VALUES
    (1, 'Grand Pets Hotel', 5),
    (2, 'Pets Heaven', 2)
-----------------------------
INSERT INTO
    dog_room(
        room_id,
        dog_id,
        hotel_id,
        register_date,
        unregister_date
    )
VALUES
    (1, 1, 1, '2020-06-08', '2020-06-10'),
    (2, 2, 2, '2020-06-10', '2020-06-15'),
    (3, 3, 2, '2020-06-20', '2020-06-23')
-----------------------------------
INSERT INTO
    cat_room(
        room_id,
        cat_id,
        hotel_id,
        register_date,
        unregister_date
    )
VALUES
    (1, 1, 1, '2020-06-08', '2020-06-10'),
    (2, 2, 2, '2020-06-10', '2020-06-15'),
    (3, 3, 2, '2020-06-20', '2020-06-23')
-----------------------------------------
SELECT * FROM dog_room
------------------------
SELECT cat_id FROM cat_room
WHERE hotel_id = 2
-------------------------
SELECT * from pet_owner
ORDER BY owner_age DESC
--------------------------
SELECT COUNT(*) from cat as count
WHERE cat_age >= 3
---------------------------------------
DELETE FROM  cat c
WHERE c.cat_age <= 2;

DELETE FROM dog d
WHERE d.dog_age <=2;
