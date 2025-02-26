import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './Navbar';
import HomePage from "../pages/HomePage";

import LoginPage from '../pages/LoginPage';
import RegisterPage from '../pages/RegisterPage';
import CreateAccountPage from '../pages/CreateAccountPage';
import TransactionPage from '../pages/TransactionPage';
import TransactionsListPage from '../pages/TransactionsListPage';

function App() {
  return (
    <Router>
      <Navbar />
      <div className="App">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/create-account" element={<CreateAccountPage />} />
          <Route path="/transactions" element={<TransactionPage />} />
          <Route path="/transactions-list" element={<TransactionsListPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
