import React from 'react';
import './AnalysisText.css';

const AnalysisText = ({ data, isHighlighted, size }) => {
  const { title, text } = data;
  const textClasses = `text-container ${isHighlighted ? 'highlighted' : ''} ${size}`;

  // Preserve newlines in the text
  const formattedText = text.split('\n').map((line, index) => (
    <React.Fragment key={index}>
      {line}
      <br />
    </React.Fragment>
  ));

  return (
    <div className={textClasses}>
      <h3 className="text-title">{title}</h3>
      <p className="text-content">{formattedText}</p>
    </div>
  );
};

export default AnalysisText;