import React from 'react';
import ReactPlayer from 'react-player';

const API_URL = 'http://localhost:8080'

export default function OtterList() {
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState('');
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
    setLoading(true);
    fetch(API_URL + '/feed/natureisfuckinglit')
      .then((response) => response.json())
      .then((data) => {
        const { feed } = data;
        setLoading(false);
        setData(feed);
      })
      .catch((e) => {
        setLoading(false);
        setError('fetch failed');
      });
  }, []);

  if (loading) {
    return <p>loading..</p>;
  }

  if (error !== '') {
    return <p>ERROR: {error}</p>;
  }

  return (
    <React.Fragment>
    {
        data.map((element) => {
            if (element.split('.').pop() === 'mp4') {
                return (
                    <ReactPlayer 
                    url={element} 
                    playing={true} 
                    loop={true}
                    muted={true}
                    pip={false}
                    />
                )
            } else {
                return (
                    <img src={element} alt='foo' style={{
                        width: '10%',
                        height: '20%',
                    }}/>
                )
            }
        })
    }

    </React.Fragment>
  );
};
