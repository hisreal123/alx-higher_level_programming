-- a script that creates a table second_table in the database in your MySQL server and add multiples rows.
--creating the table
CREATE TABLE IF NOT EXISTS`second_table` (`id` INT, `name` VARCHAR(256), `score` INT)

-- insterting multiple row data
INSERT INTO `second_table` (`id`, `name`, `score`)
-- VALUES
--     (1, 'John', 10), 
--     (2, 'Alex', 3), 
--     (3, 'Bob', 14), 
--     (4, 'George', 8);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);

