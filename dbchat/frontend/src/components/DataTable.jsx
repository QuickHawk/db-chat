import React from 'react';
import './DataTable.css';

const DataTableComponent = ({ data }) => {
  const { title, headers, rows } = data;

  return (
    <div className="table-container">
      <h3 className="table-title">{title}</h3>
      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              {headers.map((header, index) => (
                <th key={index}>{header}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((row, rowIndex) => (
              <tr key={rowIndex}>
                {row.map((cell, cellIndex) => (
                  <td key={cellIndex}>{String(cell)}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default DataTableComponent;