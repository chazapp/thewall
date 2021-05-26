import React, { useCallback, useEffect, useRef } from 'react';
import ReactPlayer from 'react-player';
import ReactLoading from 'react-loading';
import Gallery from 'react-photo-gallery';

const API_URL = 'http://192.168.1.15:8080'

const Feed = (props) => {
  let { query } = props;
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState('');
  const [data, setData] = React.useState([]);

  let imgCount = 0;
  let limit = useRef(25);
  let offset = useRef(0);
  let photos = useRef([])
  const nsfw = "false";
  query = "";
  const loadPhotos = () => {
    setLoading(true);
    const request = `${API_URL}/feed${query !== '' ? '/' + query : ''}?nsfw=${nsfw}&limit=${limit.current}&offset=${offset.current}`
    fetch(request)
      .then((response) => response.json())
      .then((data) => {
        const { feed } = data;
        setLoading(false);
        feed.forEach((media) => {
          const { content, post_url} = media;
            photos.current.push({
              src: content,
              width: 1,
              height: 1,
              post_url: post_url,
            });
          imgCount++;
        })
        offset.current = limit;
        limit.current += 25;
        setData(photos.current);
      })
      .catch((e) => {
        setLoading(false);
        setError('fetch failed');
      });
  }
  useEffect(loadPhotos, [imgCount, query, limit, offset]);

  const openPost = useCallback((event, { photo, index }) => {
    const { post_url } = photo;
    window.location.href= post_url;
  }, []);

  if (loading) {
    return  <ReactLoading type={'spin'} style={{ margin: 'auto', height: '5%', width: '5%'}} />

  }

  if (error !== '') {
    return <p>Error: {error}</p>;
  }

  if (data.length === 0) {
    return (<p> Ooops. No results. Adjust your query ? </p>)
  } else {
    return (
      <React.Fragment>
        <Gallery photos={data} direction={"column"} onClick={openPost} />
      </React.Fragment>
    );
  }
};


export default Feed;