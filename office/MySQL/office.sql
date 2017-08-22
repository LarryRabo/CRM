delimiter $$

create table 'usr_info'(
'id' int(11) NO NULL AUTO_INCREMENT COMMENT '用户编号，与用户账号不同',
'usrname' varchar(45) NOT NULL COMMENT  '用户名',
'email' varchar(45) DEFAULT NULL COMMENT  '邮箱，可以用于登陆',
'mobile' int(11) DEFAULT NULL COMMENT  '手机号，可以用于登录',
'createtime' date time NOT NULL DEFAULT 'current_timestamp',
primary key('id','usrname'),
unique key 'id_unique' ('id'),
unique key 'email_unique' ('email'),
unique key 'mobile_unique' ('mobile'),
)ENGINE=InnoDB default charset='utf8';