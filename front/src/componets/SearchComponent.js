import React from 'react';

const SearchComponent = () => {
  return (

    <div className="header-content container">

      <div className="header-2">
        <form className="search">
          <input placeholder="Are you cinephile?"/>
          <button className="btn-search" type="submit">Search</button>
        </form>
      </div>

    </div>
  );
};

export default SearchComponent;
