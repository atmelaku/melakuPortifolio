import React from 'react';
import ReactDOM from 'react-dom/client';
import GalleryApp from './GalleryApp'; // Import your GalleryApp component

const reactAppContainer = document.getElementById('react-app');

if (reactAppContainer) {
  ReactDOM.render(<GalleryApp />, reactAppContainer);
}
