import React from 'react';
import { BarChart as RechartsBarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import './BarChart.css';

const BarChartComponent = ({ data, isHighlighted, size }) => {
  const { title, labels, values } = data;

  const chartData = labels.map((label, index) => ({
    name: label,
    value: values[index],
  }));

  const chartClasses = `chart-container ${isHighlighted ? 'highlighted' : ''} ${size}`;

  return (
    <div className={chartClasses}>
      <h3 className="chart-title">{title}</h3>
      <ResponsiveContainer width="100%" height={300}>
        <RechartsBarChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" stroke="#444" />
          <XAxis dataKey="name" stroke="#888" />
          <YAxis stroke="#888" />
          <Tooltip contentStyle={{ backgroundColor: '#333', border: '1px solid #555' }} />
          <Legend />
          <Bar dataKey="value" fill="#8884d8" />
        </RechartsBarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default BarChartComponent;