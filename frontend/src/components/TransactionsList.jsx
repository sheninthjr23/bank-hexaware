import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TransactionsList = () => {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    const fetchTransactions = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/transactions/');
        setTransactions(response.data);
      } catch (error) {
        alert('Error fetching transactions.');
      }
    };

    fetchTransactions();
  }, []);

  return (
    <div>
      <h2>Transactions</h2>
      <ul>
        {transactions.map((transaction) => (
          <li key={transaction.id}>
            Sender ID: {transaction.sender_id} | Receiver ID: {transaction.receiver_id} | Amount: {transaction.amount}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TransactionsList;
