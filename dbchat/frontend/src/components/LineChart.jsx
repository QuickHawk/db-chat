import React from 'react';
import { LineChart as RechartsLineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import './LineChart.css';

const LineChartComponent = ({ data }) => {
  const { title, x_axis_label, y_axis_label, lines } = data;

  return (
    <div className="chart-container">
      <h3 className="chart-title">{title}</h3>
      <ResponsiveContainer width="100%" height={300}>
        <RechartsLineChart>
          <CartesianGrid strokeDasharray="3 3" stroke="#444" />
          <XAxis dataKey="x" type="number" domain={['dataMin', 'dataMax']} stroke="#888" name={x_axis_label} />
          <YAxis stroke="#888" name={y_axis_label} />
          <Tooltip contentStyle={{ backgroundColor: '#333', border: '1px solid #555' }} />
          <Legend />
          {lines.map((line, index) => (
            <Line key={index} type="monotone" data={line.points} name={line.name} dataKey="y" stroke={`#${Math.floor(Math.random()*16777215).toString(16)}`} />
          ))}
        </RechartsLineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default LineChartComponent;