import React, { useRef, useEffect } from "react";
import ReactDOM from 'react-dom';
import './index.css';

import Top from './components/Top/Top'
import GraphArea from './components/GraphArea/GraphArea'
import SideBar from './components/SideBar/SideBar'


const rootElement = document.getElementById("root");
ReactDOM.render(
  <div>
    <Top />
    <SideBar />
    {/* <GraphArea /> */}
  </div>
  , rootElement);