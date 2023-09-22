import React, {useEffect, useCallback} from "react";
import {Movies} from "./MovieComponent"
import {useGetMovies} from "../hooks/useGetMovies";
import {useSearch} from "../hooks/useSearch";
import debounce from "just-debounce-it"

function Main() {
  const {search, setSearch} = useSearch()
  const {movies, getSearch, getPopularMovies} = useGetMovies(search)

  useEffect(() => {

    if(search ==="")
      getPopularMovies()

  }, [search, setSearch]);

  const debouncedGetMovies = useCallback(
    debounce(search => {
      if(search !=="")
        getSearch({search})
    }, 300)
    , [getSearch]
  )

  const handel = (e) => {
    e.preventDefault()
    getSearch({search})

  }
  const handleSearch = (e) => {
    const input = e.target.value
    console.log(input)
    setSearch(input)
    debouncedGetMovies(input)

  }
  return (
    <>

        <div className="header-content container">

          <div className="header-2">
            <form className="search" onSubmit={handel}>
              <input onChange={handleSearch} value={search} name="search" placeholder="Are you cinephile?"/>
              <button className="btn-search" type="submit">Search</button>
            </form>
          </div>

        </div>

          <Movies movies={movies} title={search !== "" ? "Search" : "Most Popular Movies"}/>


    </>

  );
}

export default Main;
