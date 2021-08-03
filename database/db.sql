-- users.users definition

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_UN_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- users.posts definition

CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `posts_FK` (`author_id`),
  CONSTRAINT `posts_FK` FOREIGN KEY (`author_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- dbusers2.users definition

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(128) NOT NULL,
  `authenticated` tinyint(1) NOT NULL,
  `confirmation_email_sent_date` datetime DEFAULT NULL,
  `email_confirmed` tinyint(1) DEFAULT NULL,
  `email_confirmation_date` datetime DEFAULT NULL,
  `last_logged_in` datetime DEFAULT NULL,
  `registration_date` datetime DEFAULT NULL,
  `current_logged_in` datetime DEFAULT NULL,
  `role` varchar(30) DEFAULT 'user',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;