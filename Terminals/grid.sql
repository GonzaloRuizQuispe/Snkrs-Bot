CREATE DATABASE snkrs;

CREATE TABLE productos_grid(
	ID_Producto INT AUTO_INCREMENT NOT NULL,
	Nombre VARCHAR (255),
    Precio VARCHAR (255),
    URL_IMG VARCHAR (255),
    URL_WEB VARCHAR (255) NOT NULL,
    Cambios VARCHAR (50),
    Talles VARCHAR (255),
    Hora datetime,
    PRIMARY KEY (ID_Producto)
);

CREATE TABLE secciones_grid(
	ID_Seccion INT AUTO_INCREMENT NOT NULL,
	URL_Seccion VARCHAR (255) NOT NULL,
    PRIMARY KEY (ID_Seccion)
);

INSERT INTO productos_grid (URL_WEB) VALUES
('https://www.grid.com.ar/botitas-jordan-air-5-retro-moda-hombre-3160245/p');

INSERT INTO secciones_grid (URL_Seccion) VALUES
('https://www.grid.com.ar/calzado/zapatillas/Hombre?PS=24&map=c,c,specificationFilter_23&O=OrderByReleaseDateDESC');

SELECT * FROM secciones_grid;
SELECT * FROM productos_grid;

SELECT URL_WEB FROM productos_grid WHERE URL_WEB='https://www.grid.com.ar/botitas-jordan-air-5-retro-moda-hombre-3160245/p';

UPDATE productos_grid SET Cambios='Nuevo' WHERE ID_Producto =1;