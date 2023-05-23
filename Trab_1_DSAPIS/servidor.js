const express = require('express');
const mysql = require('mysql');

const bdConf = {
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'loja_dsapi',
};

const banco = mysql.createConnection(bdConf);

const app = express();
const port = 8001;

app.use(express.json());

app.post('/clientes', (req, res) => {
  const { nome, altura, nascimento, cidade_id } = req.body;

  const cliente = {
    nome,
    altura,
    nascimento,
    cidade_id,
  };

  const query = 'INSERT INTO clientes SET ?';

  banco.query(query, cliente, (error) => {
    if (error) {
      console.error('Erro ao cadastrar cliente:', error);
      res.status(500).json({ error: 'Erro ao cadastrar cliente' });
    } else {
      res.json({ message: 'Cliente cadastrado com sucesso' });
    }
  });
});

app.get('/produtos', (req, res) => {
  const query = 'SELECT * FROM produtos';

  banco.query(query, (error, results) => {
    if (error) {
      console.error('Erro ao consultar produtos:', error);
      res.status(500).json({ error: 'Erro ao consultar produtos' });
    } else {
      res.json(results);
    }
  });
});

app.post('/pedidos', (req, res) => {
  const { horario, endereco, cliente_id } = req.body;

  const pedido = {
    horario,
    endereco,
    cliente_id
  };

  const query = 'INSERT INTO pedidos SET ?';

  banco.query(query, pedido, (error) => {
    if (error) {
      console.error('Erro ao criar pedido:', error);
      res.status(500).json({ error: 'Erro ao criar pedido' });
    } else {
      res.json({ message: 'Pedido cadastrado com sucesso' });;
    }
  });
});

app.get('/pedidos', (req, res) => {
  const query =
    'SELECT pedidos.id, pedidos.horario, pedidos.endereco, clientes.nome AS cliente_nome ' +
    'FROM pedidos ' +
    'INNER JOIN clientes ON pedidos.cliente_id = clientes.id';

  banco.query(query, (error, results) => {
    if (error) {
      console.error('Erro ao consultar pedidos:', error);
      res.status(500).json({ error: 'Erro ao consultar pedidos' });
    } else {
      res.json(results);
    }
  });
});

app.post('/produtos', (req, res) => {
  const { nome, preco, quantidade, categoria_id } = req.body;

  const novoProduto = {
    nome,
    preco,
    quantidade,
    categoria_id,
  };

  const query = 'INSERT INTO produtos SET ?';

  banco.query(query, novoProduto, (error) => {
    if (error) {
      console.error('Erro ao criar produto:', error);
      res.status(500).json({ error: 'Erro ao criar produto' });
    } else {
      res.json({ message: 'Produto criado com sucesso' });
    }
  });
});

app.put('/produtos/:id', (req, res) => {
  const id = req.params.id;
  const { nome, preco, quantidade, categoria_id } = req.body;

  const atualizacaoProduto = {
    nome,
    preco,
    quantidade,
    categoria_id,
  };

  const query = 'UPDATE produtos SET ? WHERE id = ?';

  banco.query(query, [atualizacaoProduto, id], (error) => {
    if (error) {
      console.error('Erro ao atualizar produto:', error);
      res.status(500).json({ error: 'Erro ao atualizar produto' });
    } else {
      res.json({ message: 'Produto atualizado com sucesso' });
    }
  });
});

app.delete('/produtos/:id', (req, res) => {
  const id = req.params.id;

  const query = 'DELETE FROM produtos WHERE id = ?';

  banco.query(query, id, (error) => {
    if (error) {
      console.error('Erro ao excluir produto:', error);
      res.status(500).json({ error: 'Erro ao excluir produto' });
    } else {
      res.json({ message: 'Produto excluído com sucesso' });
    }
  });
});

app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
