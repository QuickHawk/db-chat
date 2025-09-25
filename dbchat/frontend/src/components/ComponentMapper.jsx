import React from 'react';
import KPICard from './KPICard';
import BarChartComponent from './BarChart';
import AnalysisText from './AnalysisText';

const ComponentMapper = ({ element }) => {
  switch (element.type) {
    case 'kpi_card':
      return <KPICard {...element} />;
    case 'bar_chart':
      return <BarChartComponent {...element} />;
    case 'analysis_text':
      return <AnalysisText {...element} />;
    default:
      console.warn(`Unknown component type: ${element.type}`);
      return <div>Unknown component type: {element.type}</div>;
  }
};

export default ComponentMapper;