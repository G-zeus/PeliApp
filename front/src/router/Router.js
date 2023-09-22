import React from "react";
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import {MovieDetail} from "../componets/MovieDetailComponent";
import HeaderComponent from "../componets/HeaderComponent";
import Main from "../componets/MainComponent";
import NotFound from "../componets/404";


export const MainRouter = () =>{

  return(
    <BrowserRouter>
      <HeaderComponent/>

      <Routes>
        <Route path="/" element={<Main/>}></Route>
        <Route path="/detail/:movieId" element={<MovieDetail/>}></Route>
        <Route path="*" element={<NotFound/>}></Route>
      </Routes>
    </BrowserRouter>

  )
}
