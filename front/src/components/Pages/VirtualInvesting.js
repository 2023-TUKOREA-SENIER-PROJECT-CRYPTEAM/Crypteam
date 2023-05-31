import React, { useEffect, useRef } from 'react';
import { createChart, CrosshairMode } from 'lightweight-charts';
import { Box } from '@mui/material';

const Chart = () => {
  const chartContainerRef = useRef(null);
  const chartInstanceRef = useRef(null);
  const lineSeriesRef = useRef(null);

  useEffect(() => {
    // WebSocket 연결
    const socket = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@kline_1m');

    // 차트 생성
    const chart = createChart(chartContainerRef.current, {
      width: 800,
      height: 400,
      crosshair: {
        mode: CrosshairMode.Normal,
      },
    });
    chartInstanceRef.current = chart;

    // 선 시리즈 생성
    const lineSeries = chart.addLineSeries();
    lineSeriesRef.current = lineSeries;

    // 실시간 데이터 처리
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      const kline = data.k;
      const time = kline.t / 1000; // Unix timestamp
      const close = parseFloat(kline.c);

      // 차트에 데이터 추가
      lineSeries.update({ time, value: close });
    };

    // 컴포넌트 언마운트 시 WebSocket 연결 해제
    return () => {
      socket.close();
    };
  }, []);

  return <Box ref={chartContainerRef} />;
};

export default Chart;
