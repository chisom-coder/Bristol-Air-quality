-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema pollution
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `pollution` ;

-- -----------------------------------------------------
-- Schema pollution
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pollution` DEFAULT CHARACTER SET utf8 ;
USE `pollution` ;

-- -----------------------------------------------------
-- Table `pollution`.`stations`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pollution`.`stations` ;

CREATE TABLE IF NOT EXISTS `pollution`.`stations` (
  `station` INT NOT NULL,
  `Location` VARCHAR(48) NOT NULL,
  `geo_point_2d` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`station`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pollution`.`Readings`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pollution`.`Readings` ;

CREATE TABLE IF NOT EXISTS `pollution`.`Readings` (
  `readingsid` INT NOT NULL AUTO_INCREMENT,
  `Date Time` DATETIME NOT NULL,
  `NOx` FLOAT NOT NULL,
  `NO` FLOAT NOT NULL,
  `PM10` FLOAT NOT NULL,
  `NVPM10` FLOAT NOT NULL,
  `NVPM2.5` FLOAT NOT NULL,
  `VPM10` FLOAT NOT NULL,
  `PM2.5` FLOAT NOT NULL,
  `VPM2.5` FLOAT NOT NULL,
  `CO` FLOAT NOT NULL,
  `O3` FLOAT NOT NULL,
  `SO3` FLOAT NOT NULL,
  `Temperature REAL` FLOAT NOT NULL,
  `RH` INT NOT NULL,
  `Air Pressure` INT NOT NULL,
  `DateStart DATETIME` DATETIME NOT NULL,
  `DateEnd` DATETIME NOT NULL,
  `Current` TEXT(5) NOT NULL,
  `Instrument Type` VARCHAR(32) NOT NULL,
  `Stationid` INT NOT NULL,
  PRIMARY KEY (`readingsid`),
  INDEX `Stationid_idx` (`Stationid` ASC),
  CONSTRAINT `Stationid`
    FOREIGN KEY (`Stationid`)
    REFERENCES `pollution`.`stations` (`station`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pollution`.`Schema`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pollution`.`Schema` ;

CREATE TABLE IF NOT EXISTS `pollution`.`Schema` (
  `measure` VARCHAR(32) NOT NULL,
  `description` VARCHAR(64) NOT NULL,
  `unit` VARCHAR(24) NOT NULL,
  PRIMARY KEY (`measure`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
