import React, { useState } from 'react';
import axios from 'axios';

const Transaction = () => {
  const [senderId, setSenderId] = useState('');
  const [receiverId, setReceiverId] = useState('');
  const [amount, setAmount] = useState('');

  const handleCreateTransaction = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/transactions/create', {
        sender_id: senderId,
        receiver_id: receiverId,
        amount,
      });
      alert('Transaction successful!');
    } catch (error) {
      alert('Transaction failed.');
    }
  };

  return (
    <div>
      <h2>Create Transaction</h2>
      <input
        type="number"
        placeholder="Sender ID"
        value={senderId}
        onChange={(e) => setSenderId(e.target.value)}
      />
      <input
        type="number"
        placeholder="Receiver ID"
        value={receiverId}
        onChange={(e) => setReceiverId(e.target.value)}
      />
      <input
        type="number"
        placeholder="Amount"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      <button onClick={handleCreateTransaction}>Transfer</button>
    </div>
  );
};

export default Transaction;
