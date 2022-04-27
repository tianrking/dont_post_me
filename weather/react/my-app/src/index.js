// import React from 'react';
// import ReactDOM from 'react-dom';
// import './index.css';
// import App from './App';
// import reportWebVitals from './reportWebVitals';

// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );

// // If you want to start measuring performance in your app, pass a function
// // to log results (for example: reportWebVitals(console.log))
// // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();

import React from 'react';
import ReactDOM from 'react-dom';

function Hello(props) {
  return <h1>Hello World!</h1>;
  // retrun <div id="example"></div>;
}

// ReactDOM.render(<Hello />, document.getElementById('root'));
const element = <h1>Hello, world!</h1>;
ReactDOM.render(
    element,
    <div id="example"></div>,
    document.getElementById('example')
);

