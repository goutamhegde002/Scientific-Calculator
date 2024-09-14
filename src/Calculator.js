// src/Calculator.js
import React, { useState } from "react";
import axios from "axios";

function Calculator() {
  const [operation, setOperation] = useState("");
  const [a, setA] = useState(0);
  const [b, setB] = useState(0);
  const [result, setResult] = useState(null);

  const handleCalculate = async () => {
    try {
      const response = await axios.post("http://localhost:8501/", {
        operation,
        a,
        b,
      });
      setResult(response.data);
    } catch (error) {
      console.error("Error calculating:", error);
    }
  };

  return (
    <div>
      <h1>Scientific Calculator</h1>
      <div>
        <label>Operation:</label>
        <input
          type="text"
          value={operation}
          onChange={(e) => setOperation(e.target.value)}
          placeholder="e.g., add, subtract, sin"
        />
      </div>
      <div>
        <label>First Number (a):</label>
        <input type="number" value={a} onChange={(e) => setA(e.target.value)} />
      </div>
      <div>
        <label>Second Number (b):</label>
        <input type="number" value={b} onChange={(e) => setB(e.target.value)} />
      </div>
      <button onClick={handleCalculate}>Calculate</button>
      {result && <h2>Result: {result}</h2>}
    </div>
  );
}

export default Calculator;
