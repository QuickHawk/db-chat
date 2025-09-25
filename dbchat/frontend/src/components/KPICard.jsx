import React from 'react';
import './KPICard.css';

const KPICard = ({ data, isHighlighted, size }) => {
  const { title, value, description } = data;
  const cardClasses = `kpi-card ${isHighlighted ? 'highlighted' : ''} ${size}`;

  return (
    <div className={cardClasses}>
      <h3 className="kpi-title">{title}</h3>
      <p className="kpi-value">{value}</p>
      {description && <p className="kpi-description">{description}</p>}
    </div>
  );
};

export default KPICard;