show databases;
use practisedb;
show tables;

delimiter //
create procedure sp_getall()
begin
	select * from student;
end //
delimiter ;

call sp_getall();

DELIMITER //
CREATE PROCEDURE sp_insert(IN s_name varchar(20),IN s_marks int,IN s_address varchar(30),IN s_gender varchar(5))
begin
	insert into student(name,math_marks,address,gender) values(s_name,s_marks,s_address,s_gender);
end //
delimiter ;

drop procedure sp_update;

delimiter //
create procedure sp_update(IN s_name varchar(50),In s_marks int, In s_address varchar(30),In s_gender varchar(6),IN uniqueId int)
begin
	update student set name=s_name,math_marks=s_marks,address=s_address,gender=s_gender where id=uniqueId;
end //
delimiter ;

call sp_update('Soham',65,'Mumbai','M',20);
call sp_insert('Radhs',55,'Gwalior','F');

DELIMITER //
create PROCEDURE sp_delete(IN uniqueId int)
begin
delete from student where id=uniqueId;
end //
delimiter ;
