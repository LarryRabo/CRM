CREATE TABLE `office`.`user_info` ( 
 `userid` INT NOT NULL AUTO_INCREMENT COMMENT '用户编码，',  
`user_name` VARCHAR(45) NOT NULL,  
`password` VARCHAR(45) NOT NULL COMMENT '用户密码',  
`user_email` VARCHAR(45) NULL COMMENT '用户邮箱，唯一，可以用于登陆',  
`user_mobile` VARCHAR(45) NOT NULL COMMENT '用户手机号，可以用于登陆',  
`user_type` INT NOT NULL DEFAULT 0 COMMENT '用户类型：\n3 superadmin：超级管理员\n2 admin：系统管理员\n1 master：经理级用户\n0 normal：普通用户',  
`user_createtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '用户注册时间',
  `user_updatetime` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '用户信息更新时间',  
PRIMARY KEY (`userid`),  
UNIQUE INDEX `userid_UNIQUE` (`userid` ASC),  
UNIQUE INDEX `user_email_UNIQUE` (`user_email` ASC),  
UNIQUE INDEX `user_mobile_UNIQUE` (`user_mobile` ASC)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin
COMMENT = '用户信息登陆表';