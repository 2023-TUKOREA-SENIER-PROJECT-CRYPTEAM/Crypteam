import React from 'react';

function NewsItem(props) {
  const { title, date, url } = props;

  const handleTitleClick = () => {
    window.open(url, '_blank');
  };

  return (
    <div>
      <h3 onClick={handleTitleClick}>{title}</h3>
      <p>{date}</p>
    </div>
  );
}

export default NewsItem;
