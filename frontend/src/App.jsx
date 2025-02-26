import React from 'react';
import Login from './components/Login';
import Register from './components/Register';
import CreateAccount from './components/CreateAccount';
import Transaction from './components/Transaction';
import TransactionsList from './components/TransactionsList';

function App() {
  return (
    <div className="App">
      <h1>Banking System</h1>
      <Login />
      <Register />
      <CreateAccount />
      <Transaction />
      <TransactionsList />
    </div>
  );
}

export default App;
