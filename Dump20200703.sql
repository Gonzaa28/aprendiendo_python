-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema aprendiendo_python
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema aprendiendo_python
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `aprendiendo_python` DEFAULT CHARACTER SET utf8 ;
USE `aprendiendo_python` ;

-- -----------------------------------------------------
-- Table `aprendiendo_python`.`ubicacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aprendiendo_python`.`ubicacion` (
  `idUbicacion` INT NOT NULL AUTO_INCREMENT,
  `latitud` DOUBLE NULL,
  `longitud` DOUBLE NULL,
  `pais` VARCHAR(45) NULL,
  `provincia` VARCHAR(45) NULL,
  `direccion` VARCHAR(45) NULL,
  PRIMARY KEY (`idUbicacion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aprendiendo_python`.`aeropuerto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aprendiendo_python`.`aeropuerto` (
  `idaeropuerto` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `saldo` FLOAT NULL,
  `ubicacion` INT NULL,
  PRIMARY KEY (`idaeropuerto`),
  INDEX `fk_aeropuerto_ubicacion1_idx` (`ubicacion` ASC),
  CONSTRAINT `fk_aeropuerto_ubicacion1`
    FOREIGN KEY (`ubicacion`)
    REFERENCES `aprendiendo_python`.`ubicacion` (`idUbicacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aprendiendo_python`.`piloto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aprendiendo_python`.`piloto` (
  `idpiloto` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `dni` VARCHAR(45) NULL,
  `legajo` VARCHAR(45) NULL,
  `sueldo` FLOAT NULL,
  `esta_en` INT NULL,
  PRIMARY KEY (`idpiloto`),
  INDEX `fk_piloto_aeropuerto1_idx` (`esta_en` ASC),
  CONSTRAINT `fk_piloto_aeropuerto1`
    FOREIGN KEY (`esta_en`)
    REFERENCES `aprendiendo_python`.`aeropuerto` (`idaeropuerto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aprendiendo_python`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aprendiendo_python`.`usuario` (
  `idusuario` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`idusuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aprendiendo_python`.`pasajero`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aprendiendo_python`.`pasajero` (
  `idpasajero` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `dni` VARCHAR(45) NULL,
  `saldo` FLOAT NULL,
  `es_viajero_frecuente` TINYINT NULL,
  `usuario` INT NULL,
  PRIMARY KEY (`idpasajero`),
  INDEX `fk_pasajero_usuario1_idx` (`usuario` ASC),
  CONSTRAINT `fk_pasajero_usuario1`
    FOREIGN KEY (`usuario`)
    REFERENCES `aprendiendo_python`.`usuario` (`idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aprendiendo_python`.`marca`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aprendiendo_python`.`marca` (
  `idmarca` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idmarca`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aprendiendo_python`.`modelo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aprendiendo_python`.`modelo` (
  `idmodelo` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `cantidad_asientos` INT NULL,
  `coste` FLOAT NULL,
  `fecha_fabricacion` DATE NULL,
  `marca` INT NULL,
  PRIMARY KEY (`idmodelo`),
  INDEX `fk_modelo_marca_idx` (`marca` ASC),
  CONSTRAINT `fk_modelo_marca`
    FOREIGN KEY (`marca`)
    REFERENCES `aprendiendo_python`.`marca` (`idmarca`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aprendiendo_python`.`avion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aprendiendo_python`.`avion` (
  `idavion` INT NOT NULL AUTO_INCREMENT,
  `ultimo_mantenimiento` DATE NULL,
  `modelo` INT NULL,
  `esta_en` INT NULL,
  PRIMARY KEY (`idavion`),
  INDEX `fk_avion_modelo1_idx` (`modelo` ASC),
  INDEX `fk_avion_aeropuerto2_idx` (`esta_en` ASC),
  CONSTRAINT `fk_avion_modelo1`
    FOREIGN KEY (`modelo`)
    REFERENCES `aprendiendo_python`.`modelo` (`idmodelo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_avion_aeropuerto2`
    FOREIGN KEY (`esta_en`)
    REFERENCES `aprendiendo_python`.`aeropuerto` (`idaeropuerto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aprendiendo_python`.`vuelo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aprendiendo_python`.`vuelo` (
  `idvuelo` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NULL,
  `asientos_libres` INT NULL,
  `precio` FLOAT NULL,
  `completado` TINYINT NULL,
  `origen` INT NOT NULL,
  `destino` INT NOT NULL,
  `avion` INT NULL,
  PRIMARY KEY (`idvuelo`),
  INDEX `fk_vuelo_aeropuerto1_idx` (`origen` ASC),
  INDEX `fk_vuelo_aeropuerto2_idx` (`destino` ASC),
  INDEX `fk_vuelo_avion1_idx` (`avion` ASC),
  CONSTRAINT `fk_vuelo_aeropuerto1`
    FOREIGN KEY (`origen`)
    REFERENCES `aprendiendo_python`.`aeropuerto` (`idaeropuerto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_vuelo_aeropuerto2`
    FOREIGN KEY (`destino`)
    REFERENCES `aprendiendo_python`.`aeropuerto` (`idaeropuerto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_vuelo_avion1`
    FOREIGN KEY (`avion`)
    REFERENCES `aprendiendo_python`.`avion` (`idavion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aprendiendo_python`.`vuelo_has_piloto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aprendiendo_python`.`vuelo_has_piloto` (
  `vuelo_idVuelo` INT NOT NULL,
  `piloto_idpiloto` INT NOT NULL,
  PRIMARY KEY (`vuelo_idVuelo`, `piloto_idpiloto`),
  INDEX `fk_vuelo_has_piloto_piloto1_idx` (`piloto_idpiloto` ASC),
  INDEX `fk_vuelo_has_piloto_vuelo1_idx` (`vuelo_idVuelo` ASC),
  CONSTRAINT `fk_vuelo_has_piloto_vuelo1`
    FOREIGN KEY (`vuelo_idVuelo`)
    REFERENCES `aprendiendo_python`.`vuelo` (`idvuelo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_vuelo_has_piloto_piloto1`
    FOREIGN KEY (`piloto_idpiloto`)
    REFERENCES `aprendiendo_python`.`piloto` (`idpiloto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aprendiendo_python`.`vuelo_has_pasajero`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aprendiendo_python`.`vuelo_has_pasajero` (
  `vuelo_idVuelo` INT NOT NULL,
  `pasajero_idpasajero` INT NOT NULL,
  PRIMARY KEY (`vuelo_idVuelo`, `pasajero_idpasajero`),
  INDEX `fk_vuelo_has_pasajero_pasajero1_idx` (`pasajero_idpasajero` ASC),
  INDEX `fk_vuelo_has_pasajero_vuelo1_idx` (`vuelo_idVuelo` ASC),
  CONSTRAINT `fk_vuelo_has_pasajero_vuelo1`
    FOREIGN KEY (`vuelo_idVuelo`)
    REFERENCES `aprendiendo_python`.`vuelo` (`idvuelo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_vuelo_has_pasajero_pasajero1`
    FOREIGN KEY (`pasajero_idpasajero`)
    REFERENCES `aprendiendo_python`.`pasajero` (`idpasajero`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
