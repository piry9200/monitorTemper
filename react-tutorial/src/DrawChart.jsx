import React from 'react'
import { Line } from 'react-chartjs-2';
import { Chart, registerables } from "chart.js"
Chart.register(...registerables)

const DrawChart = (props) => {
    const graphData= {
          // 軸ラベル
          // 各ラベルを配列にすることで軸ラベルが改行されて表示される
        labels: props.labels,
        datasets: [
          // 表示するデータセット
          {
            data: props.temperature,
            label: props.labelTemp,
            backgroundColor: 'rgba(270, 145, 153, 1)',
            borderColor: 'rgba(240, 145, 153, 1)',
            yAxisID: 'temperature'
          },
          {
            data: props.humidity,
            label: props.labelHumi,
            backgroundColor: 'rgba(137, 195, 265, 1)',
            borderColor: 'rgba(137, 195, 235, 1)',
            yAxisID: 'humidity'
          }
        ],
        options:{
            responsive: true,
            scales: {
                'temperature': {
                    position: 'left'
                },
                'humidity': {
                    position: 'right'
                }
            }
        }
      };
  return (
    <>
        <Line data={graphData} />
    </>
  );
}

export default DrawChart