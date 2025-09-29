import React from 'react';
import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import './ScatterPlot.css';

const ScatterPlotComponent = ({ data }) => {
  const { title, x_axis_label, y_axis_label, points } = data;

  return (
    <div className="chart-container">
      <h3 className="chart-title">{title}</h3>
      <ResponsiveContainer width="100%" height={300}>
        <ScatterChart>
          <CartesianGrid strokeDasharray="3 3" stroke="#444" />
          <XAxis dataKey="x" type="number" name={x_axis_label} stroke="#888" />
          <YAxis dataKey="y" type="number" name={y_axis_label} stroke="#888" />
          <Tooltip cursor={{ strokeDasharray: '3 3' }} contentStyle={{ backgroundColor: '#333', border: '1px solid #555' }} />
          <Legend />
          <Scatter name="Data Points" data={points} fill="#8884d8" />
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ScatterPlotComponent;