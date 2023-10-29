CREATE TABLE Clientes
(
    ID SERIAL PRIMARY KEY,
    Nome VARCHAR(100),
    Email VARCHAR(100),
    DataDeRegistro TIMESTAMP
);
INSERT INTO Clientes (ID, Nome, Email, DataDeRegistro)
VALUES 
		(1, 'João', 'joao@email.com', '2023-10-29'),
       (2, 'Maria', 'maria@email.com', '2023-10-29'),
       (3, 'Carlos', 'carlos@email.com', '2023-10-30'),
       (4, 'Matheus', 'Matheus@email.com', '2023-10-29'),
       (5, 'Yuri', 'Yuri@email.com', '2023-10-29');

SELECT * FROM Clientes WHERE DATE(DataDeRegistro) = '2023-10-29';

CREATE OR REPLACE FUNCTION total_customers(date DATE)
RETURNS INTEGER AS $$
DECLARE
    total INTEGER;
BEGIN
    SELECT COUNT(*) INTO total
    FROM Clientes
    WHERE DATE(DataDeRegistro) = date;
    RETURN total;
END; $$
LANGUAGE plpgsql;

SELECT total_customers('2023-10-29');