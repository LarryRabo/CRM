delimiter $$

#drop table user_info; #删除数据

INSERT INTO user_info (user_name,password,user_email,user_mobile,user_type)
                       VALUES
					( 'superadmin','123456','rabo2014@163.com','17621622663','3'),( 'admin','123456','rabo2015@163.com','17621622662','2'),
( 'master','123456','rabo2016@163.com','17621622661','1'),
( 'normal','123456','rabo2017@163.com','17621622660','0');
