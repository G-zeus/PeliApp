import {useNavigate} from 'react-router-dom';

const MovieContainer = ({movies, title = "Most Popular"}) =>{

  const navigate = useNavigate();
  const handleOnClick = (e) => {
    e.preventDefault()
    const id = e.target.id
    console.log(id)
    navigate(`/detail/${id}`)
  };

  return (
    <>
      <section className="movies container">
        <h2>{title}</h2>
        <hr/>
        <div className="box-container-1">
          {
            movies.map(movie => (
              <div key={movie.id} className="box-container-1">
                <div className="box-1">
                  <div className="content">
                    <img src={movie.posterImage} id={movie.id} alt={movie.title} onClick={handleOnClick}/>
                    <h3>{movie.title} <strong>{`(${movie.releaseYear})`}</strong></h3>
                    <p>{movie.overview}</p>
                  </div>
                  <div   className="load-more" id={movie.id} onClick={handleOnClick}>More... </div>
                </div>

              </div>
            ))
          }
        </div>
      </section>
    </>
  )

}


const NoDataResult = () => {
  return (

    <div className="wrapper">
      <div className="main_card">
        <h1>404</h1>
        <p className="year">No Search Result</p>

      </div>


    </div>
  )
}


export function Movies({movies, info, title }) {
  const hasData = movies?.length > 0
  const hasInfo = info?.length > 0

  return (hasData && !hasInfo ? <MovieContainer movies={movies} title={title}/> : <NoDataResult/>)
}
