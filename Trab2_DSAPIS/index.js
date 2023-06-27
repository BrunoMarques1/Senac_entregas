const express = require('express');
const mysql = require('mysql');

const bdConf = {
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'tarefas',
};

const banco = mysql.createConnection(bdConf);

banco.connect((error) => {
  if (error) {
    console.error('Erro ao conectar ao banco de dados:', error);
    return;
  }
  console.log('Conexão bem-sucedida ao banco de dados');
});

const app = express();
const port = 8001;

app.use(express.json());

app.post('/cadastrar', (req, res) => {
  const { aluno, materia, professor, data_entrega, descricao, entregue } = req.body;

  const tarefa = {
    aluno,
    materia,
    professor,
    data_entrega,
    descricao,
    entregue,
  };

  const query = 'INSERT INTO tarefa SET ?';

  banco.query(query, tarefa, (error) => {
    if (error) {
      console.error('Erro ao cadastrar tarefa:', error);
      res.status(500).json({ error: 'Erro ao cadastrar tarefa' });
    } else {
      res.json({ message: 'Tarefa cadastrada com sucesso' });
    }
  });
});

app.get('/tarefas', (req, res) => {
  const query =
    'SELECT aluno, materia, professor, data_entrega, descricao, entregue ' +
    'FROM tarefa';

  banco.query(query, (error, results) => {
    if (error) {
      console.error('Erro ao consultar tarefas:', error);
      res.status(500).json({ error: 'Erro ao consultar tarefas' });
    } else {
      res.json(results);
    }
  });
});

app.put('/tarefas/:id', (req, res) => {
    const id = req.params.id;
    const {aluno, materia, professor, data_entrega, descricao, entregue } = req.body;
    
    const query = 'UPDATE tarefa SET materia=?, professor=?, data_entrega=?, descricao=?, entregue=? WHERE id=?';
    const values = {aluno, materia, professor, data_entrega, descricao, entregue};
  
    banco.query(query, [values, id], (error, results) => {
      if (error) {
        console.error('Erro ao atualizar tarefa:', error);
        res.status(500).json({ error: 'Erro ao atualizar tarefa' });
      } else {
        res.json({ message: 'Tarefa atualizada com sucesso' });
      }
    });
  });
  

app.delete('/tarefas/:id', (req, res) => {
    const id = req.params.id;
  
    const query = 'DELETE FROM tarefa WHERE id=?';
  
    banco.query(query, id, (error, results) => {
      if (error) {
        console.error('Erro ao excluir tarefa:', error);
        res.status(500).json({ error: 'Erro ao excluir tarefa' });
      } else {
        res.json({ message: 'Tarefa excluída com sucesso' });
      }
    });
  });
  

app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
