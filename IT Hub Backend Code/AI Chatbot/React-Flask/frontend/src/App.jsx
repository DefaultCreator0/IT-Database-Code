import React, { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    if (!isOpen) return;

    const fetchInitialMessage = async () => {
      try {
        const response = await axios.get("http://localhost:5000/Fetch");
        const initialBotMessage = { sender: "AI", text: response.data };
        setMessages([initialBotMessage]);
      } catch (error) {
        console.error("Error fetching initial message from chatbot API", error);
      }
    };

    fetchInitialMessage();
  }, [isOpen]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    try {
      const response = await axios.post("http://localhost:5000/post", { message: input });
      const botMessage = { sender: "AI", text: response.data };
      const httpStartVal=0;
      let link ="";
      let counter =-1;
      console.log(response.data.type);
      if (response.data.includes("storage.")){
        for(let i = 0;i < response.data.length;i++){
          if(response.data[i].includes(":")){
            counter = i;
            i=i+2;
          }
          if(counter != -1){
            link = link + response.data[i];
          }
        }
        link = "https://"+link;
        console.log(link)
        window.open(link);
        
      }
      if(response.data.includes("http://localhost:5173")){
        window.open("http://localhost:5173");
      }
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error("Error communicating with the chatbot API", error);
    }
  };

  return (
    <>
      <button className="chat-toggle-button" onClick={() => setIsOpen(!isOpen)}>
        {isOpen ? "Close Chat" : "Open Chat"}
      </button>

      {isOpen && (
        <div className="chat-popup">
          <div className="chat-header">Chatbot</div>

          <div className="chat-body">
            {messages.map((msg, index) => (
              <div
                key={index}
                className={`chat-message ${msg.sender === "user" ? "user" : "bot"}`}
              >
                <strong>{msg.sender}:</strong> {msg.text}
              </div>
            ))}
          </div>

          <div className="chat-input-container">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === "Enter" && sendMessage()}
              placeholder="Type a message..."
            />
            <button className="SendButton" onClick={sendMessage}>Send</button>
          </div>
        </div>
      )}
    </>
  );
};

export default Chatbot;
