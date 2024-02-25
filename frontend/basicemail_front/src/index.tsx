import './index.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { ActualViewProvider } from './Contexts/ViewContext';

const rootElement = document.getElementById('root');
const root = ReactDOM.createRoot(rootElement as HTMLElement); // Cast to HTMLElement
root.render(
  <React.StrictMode>
    <ActualViewProvider>
      <App />
    </ActualViewProvider>
  </React.StrictMode>
)