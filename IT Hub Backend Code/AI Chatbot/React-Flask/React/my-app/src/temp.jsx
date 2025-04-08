// Filename - App.js

// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";
import {QueryClient, QueryClientProvider, useQuery} from '@tanstack/react-query'
//Figure this out, I am tired
// Look Here https://tanstack.com/query/latest/docs/framework/react/reference/useQuery

function handleSubmit(e) {
    e.preventDefault();
        const form = e.target;
    const formData = new FormData(form);

    const formJson = Object.fromEntries(formData.entries());

    const postdata = formJson;
    fetch('http://localhost:5000/post', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postdata)
    })
        .then(response => response.json())
        .then(result => console.log(result));
    this.Input.value="";
    getInfo
}

function getInfo(){
    const [data, setdata] = useState({
        UserInput: "",
        AIInput: ""
    });
    const [count,setCount] = useState(0);
    useEffect(() => {
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy        
        fetch('http://localhost:5000/Fetch').then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setdata({UserInput: data.UserInput, AIInput:data.AIInput});
                setCount(count => count+1);
            })
        );
    },[count]);
    return data
}

function App() {
    const USI = getInfo()["UserInput"]
    const AIO = getInfo()["AIInput"]


    return (
        <div className="App">
            <header className="App-header">
                <h1>React and flask</h1>
                {/* Calling a data from setdata for showing */}
                <p>User Input : {USI}"</p>
                <p>AI Input : {AIO}</p>
                <form onSubmit={handleSubmit}>
                    <input name="Input" placeholder="Input Here" type="text"></input>
                    <button type="submit"></button>
                </form>
            </header>
        </div>
    );
}

export default App;
