CREATE TABLE productos_digitalsport(
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

CREATE TABLE secciones_digitalsport(
	ID_Seccion INT AUTO_INCREMENT NOT NULL,
	URL_Seccion VARCHAR (255) NOT NULL,
    PRIMARY KEY (ID_Seccion)
);

SELECT * FROM secciones_digitalsport;
SELECT * FROM productos_digitalsport;

INSERT INTO productos_digitalsport (URL_WEB) VALUES
('https://www.digitalsport.com.ar/dionysos/prod/zapatillas-superstar-adidas-539125/');