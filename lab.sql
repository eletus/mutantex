
CREATE TABLE `stat_adn` (
  `id_adn` int NOT NULL AUTO_INCREMENT,
  `type_adn` varchar(30) NOT NULL,
  `name_adn` varchar(30) NOT NULL,
  `cur_date` timestamp NULL DEFAULT NULL,
  `digest` varchar(64) NOT NULL,
  PRIMARY KEY (`name_adn`),
  KEY `id_adn` (`id_adn`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
