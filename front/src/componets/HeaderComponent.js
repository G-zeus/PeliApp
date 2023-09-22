import React from 'react';

const HeaderComponent = () => {
  return (
   <>
     <header className="header">
       <div className="menu container">
         <a href="http://localhost:3000" className="logo">PeliApp </a>
         <input type="checkbox" id="menu"/>
         <label htmlFor="menu">
         </label>
         <nav className="navbar">
           <ul>
             <li>
               <a href="http://localhost:3000">Home</a>
             </li>
           </ul>
         </nav>
       </div>
     </header>
   </>

  );
};

export default HeaderComponent;
