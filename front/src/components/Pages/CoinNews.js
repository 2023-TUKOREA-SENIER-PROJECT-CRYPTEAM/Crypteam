/*eslint-disable*/
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {  Box,Grid, Typography, TextField, Paper,Button,TableCell, TableContainer, Table, TableRow } from '@mui/material';
//import NewsItem from '../NewsItem';

function CoinNews() {
  const [newsdata, setNewsData] = useState([]);

  const [searchValue, setSearchValue] = useState('');
  const [selectedCoin, setSelectedCoin] = useState('전체');

  useEffect(() => {
    async function fetchNewsData() {
      const response = await axios.get('http://127.0.0.1:8000/api/news');
      setNewsData(response.data);
    }
    fetchNewsData();
  }, []);

  const coins = ['전체', '비트코인', '이더리움', '이더리움 클래식', '리플', '카르다노 에이다'];
  const handleCoinClick = (coin_name) => {
        setSelectedCoin(coin_name);
    };
    const filteredCoins = newsdata.filter((newsdata) => {
        if (selectedCoin === '전체') {
            return newsdata.news_title.toLowerCase().includes(searchValue.toLowerCase());
        } else {
            return newsdata.coin_name === selectedCoin && newsdata.news_title.toLowerCase().includes(searchValue.toLowerCase());
        }
    });



  return (
    <div>
        <Typography variant="h5" sx={{ marginBottom: 2 }}>
            코인동향            
            <Box sx={{ display: 'flex', flexDirection: 'row' }}>
                {coins.map((coin_name) => (
                     <Typography
                     key={coin_name}
                     sx={{ marginRight: 1, marginBottom: 1, cursor: 'pointer' }}
                     onClick={() => handleCoinClick(coin_name)}
                     >
                     {coin_name}
                     </Typography>
                 ))}
             </Box>                        
        </Typography>

        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="a dense table">
              <TableRow>
                <TableCell sx={{ fontWeight: 'bold', borderBottomWidth: 2 }}>No.</TableCell>
                <TableCell sx={{ fontWeight: 'bold', borderBottomWidth: 2 }}>제목</TableCell>
                <TableCell sx={{ fontWeight: 'bold', borderBottomWidth: 2 }}>날짜</TableCell>
                <TableCell sx={{ fontWeight: 'bold', borderBottomWidth: 2 }}>코인</TableCell>
              </TableRow>

              {filteredCoins.map((newsdata,index) => (
              <TableRow key={newsdata.id}>
                  <TableCell component="th" scope="row" sx={{ borderBottomWidth: 2 }}>
                  {index + 1}
                  </TableCell>
                  <TableCell onClick={() => window.open(newsdata.news_url, '_blank')} sx={{ borderBottomWidth: 2 }}>{newsdata.news_title}</TableCell>
                  <TableCell sx={{ borderBottomWidth: 2 }}>{newsdata.news_registered_date}</TableCell>
                  <TableCell sx={{ borderBottomWidth: 2 }}>{newsdata.coin_name}</TableCell>
              </TableRow>
              ))}
            </Table>
            </TableContainer>
        
    </div>
  );
}

export default CoinNews;


// import React, {useState, useEffect} from 'react';
// import axios from 'axios';
// import {Link} from 'react-router-dom';
// import {  Box,Grid, Typography, List, ListItem, ListItemText, ListItemSecondaryAction } from '@mui/material';

// const CoinNews = () => {

//     const[newsData, setNewsData] = useState([]);
//     const NewsItem = ({id, title, coin, date, url})=>{
//         const handleClick = () =>{
//             window.open(url,'_blank');
//         };
//         return (
//             <Typography key={id} sx={{ marginBottom: 1, cursor: 'pointer' }} onClick={handleClick}>
//               [{coin}] {title} ({date})
//             </Typography>
//           );
//     }
//     const coins = ['전체', 'BTC', '이더리움', '거래소3', '거래소4'];
//     const handleCoinClick = (coin) => {
//         setSelectedCategory(coin);
//       };

//     useEffect(() =>{
//         axios
//             .get('')
//             .then((response)=>{
//                 setNewsData(response.newsdata);
//             })
//             .catch(error=>{
//                 console.log(error);
//             });
//     },[]);

    

//     return(
//         <>
//         <Typography variant="h5" sx={{ marginBottom: 2 }}>
//             거래소별 코인동향            
//             <Box sx={{ display: 'flex', flexDirection: 'row' }}>
            
//                 {coins.map((coin) => (
//                     <Typography
//                     key={coin}
//                     sx={{ marginRight: 1, marginBottom: 1, cursor: 'pointer' }}
//                     onClick={() => handleCoinClick(coin)}
//                     >
//                     {coin}
//                     </Typography>
//                 ))}
//             </Box>                        
//         </Typography>
        
//         <List>        
//         {newsData.map((news) => (
//             <ListItem key={news.id} button component={Link} to={news.url}>
//             <ListItemText
//                 primary={news.title}
//                 secondary={`${news.exchange} | ${news.date}`}
//             />
//             <ListItemSecondaryAction>
//                 <Typography>{news.name}</Typography>
//             </ListItemSecondaryAction>
//             </ListItem>
//         ))}
//         </List>
        
//         </>

//     )
// };

// export default CoinNews;
