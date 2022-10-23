import React, { useEffect } from 'react';
import DrawChart from './DrawChart';
import { useState } from 'react';

async function referJsonOfTemper(){
    const response = await fetch("http://127.0.0.1:5000/get");
	const json = await response.json();
    const {date:labels, temperature:temperatures, humidity:humidities} = json;
    const arrayOfAll = [labels, temperatures, humidities]
    return arrayOfAll
}

function App() {
    const [labels, setLabels] = useState();
    const [temperature, setTemperature] = useState();
    const [humidity, setHumidity] = useState();

    useEffect(() => {
        referJsonOfTemper().then(result => {
            setLabels(result[0])
            setTemperature(result[1])
            setHumidity(result[2])
        })
    }, [])
    const labelTemp = '温度';
    const labelHumi = '湿度';

    return (
      <>
        < DrawChart labels ={labels} temperature = {temperature} humidity = {humidity} labelTemp = {labelTemp} labelHumi = {labelHumi} />
      </>
    )
}
  
  export default App
