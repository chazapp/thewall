import React from 'react';
import ReactPlayer from 'react-player';
import ReactLoading from 'react-loading';
import Gallery from 'react-photo-gallery';
const API_URL = 'http://192.168.1.15:8080'

export default function Feed(props) {
  const { query } = props;
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState('');
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    setLoading(true);
    fetch(`${API_URL}/feed/${query !== "" ? query : "pics"}`)
      .then((response) => response.json())
      .then((data) => {
        const { feed } = data;
        setLoading(false);
        let photos= [];
        feed.forEach((link) => {
          photos.push({
            src: link,
            width: 1,
            height: 1
          })
        })
        setData(photos);
      })
      .catch((e) => {
        setLoading(false);
        setError('fetch failed');
      });
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
        <Gallery photos={data} />
      </React.Fragment>
    );
  }
};


     // data.map((element, index) => {
        //     if (element.split('.').pop() === 'mp4') {
        //         return (
        //             <ReactPlayer 
        //             url={element} 
        //             playing={true} 
        //             loop={true}
        //             muted={true}
        //             pip={false}
        //             key={index}
        //             />
        //         )
        //     } else {
        //         return (
        //             <img src={element} alt='foo' style={{
        //                 width: '10%',
        //                 height: '20%',
        //             }}
        //             key={index}
        //             />
        //         )
        //     }
        // })