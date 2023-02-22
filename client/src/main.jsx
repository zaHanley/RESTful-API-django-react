import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import Header from "./components/Header";
import Footer from "./components/Footer";
import "bootswatch/dist/simplex/bootstrap.min.css"
import "./index.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

ReactDOM.createRoot(document.getElementById("root")).render(
  
  <Router>
    {/* <React.StrictMode> */}
      <Header />
      <Routes>
        <Route exact path="/" element={<App />} />
      </Routes>
      <Footer />
      {/* </React.StrictMode> */}
  </Router>
  
);
