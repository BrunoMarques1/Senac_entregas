CREATE DATABASE tarefas;
USE tarefas;
-- DROP DATABASE tarefas;
CREATE TABLE tarefa(
	id INT NOT NULL AUTO_INCREMENT,
	aluno VARCHAR(90) NOT NULL,
	materia VARCHAR(30) NOT NULL, 
    professor VARCHAR(90),
    data_entrega DATE NOT NULL, 
    descricao VARCHAR(200),
    entregue VARCHAR(100) NOT NULL,
    PRIMARY KEY(id)
);

select * from tarefa