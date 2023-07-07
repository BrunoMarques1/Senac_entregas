const express = require('express');
const mysql = require('mysql');
const axios = require('axios');

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

app.post('/cadastrar', async (req, res) => {
  const { aluno, materia, professor, data_entrega, descricao, entregue } = req.body;

  const token = req.header('Authorization').replace('Bearer ', '');

  try {
    const response = await axios.get('https://api.github.com/user', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const { login: usuario } = response.data;

    const tarefa = {
      usuario,
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
  } catch (error) {
    console.error('Erro ao obter detalhes do usuário:', error);
    res.status(500).json({ error: 'Erro ao obter detalhes do usuário' });
  }
});

app.get('/mostrar', async (req, res) => {
  const token = req.header('Authorization').replace('Bearer ', '');

  try {
    const response = await axios.get('https://api.github.com/user', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const { login: usuario } = response.data;

    const query =
      'SELECT id, aluno, materia, professor, data_entrega, descricao, entregue ' +
      'FROM tarefa WHERE usuario = ?';

    banco.query(query, [usuario], (error, results) => {
      if (error) {
        console.error('Erro ao consultar tarefas:', error);
        res.status(500).json({ error: 'Erro ao consultar tarefas' });
      } else {
        res.json(results);
      }
    });
  } catch (error) {
    console.error('Erro ao obter detalhes do usuário:', error);
    res.status(500).json({ error: 'Erro ao obter detalhes do usuário' });
  }
});

app.put('/tarefas/:id', async (req, res) => {
  const { id } = req.params;
  const { aluno, materia, professor, data_entrega, descricao, entregue } = req.body;

  const token = req.header('Authorization').replace('Bearer ', '');

  try {
    const response = await axios.get('https://api.github.com/user', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const { login: usuario } = response.data;

    const query =
      'UPDATE tarefa SET aluno=?, materia=?, professor=?, data_entrega=?, descricao=?, entregue=? ' +
      'WHERE id=? AND usuario=?';

    const values = [aluno, materia, professor, data_entrega, descricao, entregue, id, usuario];

    banco.query(query, values, (error, results) => {
      if (error) {
        console.error('Erro ao atualizar tarefa:', error);
        res.status(500).json({ error: 'Erro ao atualizar tarefa' });
      } else {
        res.json({ message: 'Tarefa atualizada com sucesso' });
      }
    });
  } catch (error) {
    console.error('Erro ao obter detalhes do usuário:', error);
    res.status(500).json({ error: 'Erro ao obter detalhes do usuário' });
  }
});

app.delete('/tarefas/:id', async (req, res) => {
  const { id } = req.params;
  const token = req.header('Authorization').replace('Bearer ', '');

  try {
    const response = await axios.get('https://api.github.com/user', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const { login: usuario } = response.data;

    const query = 'DELETE FROM tarefa WHERE id=? AND usuario=?';
    const values = [id, usuario];

    banco.query(query, values, (error, results) => {
      if (error) {
        console.error('Erro ao excluir tarefa:', error);
        res.status(500).json({ error: 'Erro ao excluir tarefa' });
      } else {
        res.json({ message: 'Tarefa excluída com sucesso' });
      }
    });
  } catch (error) {
    console.error('Erro ao obter detalhes do usuário:', error);
    res.status(500).json({ error: 'Erro ao obter detalhes do usuário' });
  }
});


app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
