import React from 'react';
import KPICard from './KPICard';
import BarChartComponent from './BarChart';
import AnalysisText from './AnalysisText';
import LineChartComponent from './LineChart';
import PieChartComponent from './PieChart';
import DataTableComponent from './DataTable';
import ScatterPlotComponent from './ScatterPlot';


const ComponentMapper = ({ element }) => {
  switch (element.type) {
    case 'kpi_card':
      return <KPICard {...element} />;
    case 'bar_chart':
      return <BarChartComponent {...element} />;
    case 'analysis_text':
      return <AnalysisText {...element} />;
    case 'line_chart':
      return <LineChartComponent data={element.data} />;
    case 'pie_chart':
      return <PieChartComponent data={element.data} />;
    case 'data_table':
      return <DataTableComponent data={element.data} />;
    case 'scatter_plot':
      return <ScatterPlotComponent data={element.data} />;
    default:
      console.warn(`Unknown component type: ${element.type}`);
      return <div>Unknown component type: {element.type}</div>;
  }
};

export default ComponentMapper;