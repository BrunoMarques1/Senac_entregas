const express = require('express');
const passport = require('passport');
const GitHubStrategy = require('passport-github').Strategy;

const app = express();

const GITHUB_CLIENT_ID = 'effd810fb1e5e164ca9d';
const GITHUB_CLIENT_SECRET = '1ef28d0121d5e80ca23b5139744e4d59e2136cb9';
const GITHUB_CALLBACK_URL = 'http://localhost:3000/auth/github/callback';

app.use(
  require('express-session')({
    secret: 'chave',
    resave: false,
    saveUninitialized: false,
  })
);

app.use(passport.initialize());
app.use(passport.session());

passport.use(
  new GitHubStrategy(
    {
      clientID: GITHUB_CLIENT_ID,
      clientSecret: GITHUB_CLIENT_SECRET,
      callbackURL: GITHUB_CALLBACK_URL,
    },
    function (accessToken, refreshToken, profile, cb) {
      
      const user = {
        id: profile.id,
        name: profile.displayName || 'Nome não disponível',
        username: profile.username,
      };
      return cb(null, user);
    }
  )
);

passport.serializeUser(function (user, cb) {
  cb(null, user);
});

passport.deserializeUser(function (user, cb) {
  cb(null, user);
});

app.get('/auth/github', passport.authenticate('github'));

app.get(
  '/auth/github/callback',
  passport.authenticate('github', { successRedirect: '/profile', failureRedirect: '/login' })
);

app.get('/profile', (req, res) => {
  res.send(`Bem-vindo, ${req.user.name}!`);
});

app.listen(3000, () => {
  console.log('Servidor rodando em http://localhost:3000');
});
