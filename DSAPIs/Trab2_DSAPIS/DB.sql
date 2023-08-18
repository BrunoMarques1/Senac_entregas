CREATE DATABASE tarefas;
USE tarefas;
CREATE TABLE tarefa(
	id INT NOT NULL AUTO_INCREMENT,
    usuario VARCHAR(90) NOT NULL,
	aluno VARCHAR(90) NOT NULL,
	materia VARCHAR(30) NOT NULL, 
    professor VARCHAR(90),
    data_entrega DATE NOT NULL, 
    descricao VARCHAR(200),
    entregue VARCHAR(100) NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO tarefa(usuario,aluno,materia,professor,data_entrega,descricao,entregue)
VALUES ("igoralves","igor","DSAPIS","Adalto","2023-11-11","Trab 2","Não");

select * from tarefa