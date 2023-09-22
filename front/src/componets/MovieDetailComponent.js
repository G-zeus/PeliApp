import {IoMdStopwatch, IoMdThumbsUp} from "react-icons/io";
import {useGetMovies} from "../hooks/useGetMovies";
import {useEffect} from "react";
import {useParams} from "react-router-dom";

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

const Detail = ({movie}) => {
    return (
        <div className="wrapper">
            <div className="main_card">
                <div className="card_left">
                    <div className="card_datails">
                        <h1>{movie.title}</h1>
                        <div className="card_cat">
                            {/*<p className="PG">PG - 13</p>*/}
                            <p className="year">{movie.releaseYear}</p>
                            <p className="genre">{movie.genres.map(v => `| ${v} | `)}</p>
                        </div>
                        <p className="disc">{movie.overview}</p>
                        <div className="social-btn">
                            <button>
                                <IoMdStopwatch/> {`${movie.runtime} M`}
                            </button>
                            <button>
                                <IoMdThumbsUp/> {movie.averageRating}
                            </button>

                        </div>
                    </div>
                </div>
                <div className="card_right">
                    <div className="img_container">
                        <img src={movie.posterImage} alt=""/>
                    </div>
                </div>
            </div>
        </div>

    )
}


export function MovieDetail() {
    const {movieId} = useParams()

    const {info, getDetail} = useGetMovies("")


    useEffect(() => {

        getDetail(movieId)
        console.log(info)
        // console.log(info.title.length)


    }, []);

    const hasData = info?.title?.length > 0


    return (hasData ? <Detail movie={info}/> : <NoDataResult/>)
}
