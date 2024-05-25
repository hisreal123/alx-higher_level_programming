-- a script that creates a table second_table in the database in your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS`second_table` (`id` INT, `name` VARCHAR(256), `score` INT)
INSERT INTO `second_table` (`id`, `name`, `score`)
VALUES ((1,2,3,4,5), ('John', 'Alex', 'Bob', 'George'), (10,3,14,8));
