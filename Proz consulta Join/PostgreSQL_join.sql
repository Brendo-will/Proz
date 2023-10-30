-- Criação da tabela 'Funcionarios'
CREATE TABLE Funcionarios (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    Cargo VARCHAR(100)
);

-- Criação da tabela 'Departamentos'
CREATE TABLE Departamentos (
    ID INT PRIMARY KEY,
    NomeDepartamento VARCHAR(100),
    IDFuncionario INT,
    FOREIGN KEY (IDFuncionario) REFERENCES Funcionarios(ID)
);

-- Inserção de dados na tabela 'Funcionarios'
INSERT INTO Funcionarios (ID, Nome, Cargo) VALUES 
(1, 'João', 'Gerente'),
(2, 'Maria', 'Analista'),
(3, 'Pedro', 'Desenvolvedor');

-- Inserção de dados na tabela 'Departamentos'
INSERT INTO Departamentos (ID, NomeDepartamento, IDFuncionario) VALUES 
(1, 'RH', 1),
(2, 'Financeiro', 2),
(3, 'TI', 3);

-- Consulta utilizando JOIN
SELECT Funcionarios.Nome, Departamentos.NomeDepartamento
FROM Funcionarios
JOIN Departamentos ON Funcionarios.ID = Departamentos.IDFuncionario;