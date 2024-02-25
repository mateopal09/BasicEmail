import './index.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { ActualViewProvider } from './Contexts/ViewContext';
import { SelectedEmailProvider } from './Contexts/SelectedEmailContext';

const rootElement = document.getElementById('root');
const root = ReactDOM.createRoot(rootElement as HTMLElement); // Cast to HTMLElement
root.render(
  <React.StrictMode>
    <SelectedEmailProvider>
      <ActualViewProvider>
        <App />
      </ActualViewProvider>
    </SelectedEmailProvider>
  </React.StrictMode>
)