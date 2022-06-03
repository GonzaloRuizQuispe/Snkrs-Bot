CREATE TABLE productos_tiendafuencarral(
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

CREATE TABLE secciones_tiendafuencarral(
	ID_Seccion INT AUTO_INCREMENT NOT NULL,
	URL_Seccion VARCHAR (255) NOT NULL,
    PRIMARY KEY (ID_Seccion)
);

SELECT * FROM secciones_tiendafuencarral;
SELECT * FROM productos_tiendafuencarral;

INSERT INTO productos_tiendafuencarral (URL_WEB) VALUES
('https://www.tiendafuencarral.com.ar/zapatillas-reebok-power-ranger-club-c-legacy-hombre-gx2826/p');