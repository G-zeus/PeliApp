import {useState, useRef, useCallback,} from "react";

export const useGetMovies = ({search}) => {
    const previousSearch = useRef(search)
    const [loading, setLoading] = useState(false)
    const [info, setInfo] = useState([])
    const [movies, setMovies] = useState([])
    const [, setError] = useState(null)

    const getPopularMovies = () => {
        fetch(`${process.env.REACT_APP_API_URL}movies/popular`)
            .then(res => res.json())
            .then(json => setMovies(json.data.movies))
    }


    const getSearch = useCallback(({search}) => {
        if (search === previousSearch.current) return

        setLoading(true)
        setError(null)
        previousSearch.current = search
        fetch(`${process.env.REACT_APP_API_URL}movies/find?search=${search}`)
            .then(res => res.json())
            .then(json => setMovies(json.data.movies))
            .catch(e => setError(e.message))
            .finally(setLoading(false))

    }, [])

    const getDetail = (id) => {
        fetch(`${process.env.REACT_APP_API_URL}movies/${id}`)
            .then(res => res.json())
            .then(json => setInfo(json.data.movie))
            .catch(e => setError(e.message))

    }

    return {movies, loading, info, setInfo, getDetail, getSearch, getPopularMovies}
}



