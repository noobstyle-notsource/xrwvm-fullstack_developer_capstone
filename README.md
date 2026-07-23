# Cars Dealership - Full-stack Capstone Project

Welcome to the **Cars Dealership** web application! This repository contains the complete full-stack web application developed for a national car retailer in the U.S.

## Overview
The application allows users to view nationwide dealership branches, filter dealerships by state, read customer reviews, post new reviews with sentiment analysis, and manage car makes and models through a Django admin dashboard.

## Tech Stack & Architecture
- **Frontend**: React.js, Bootstrap 5, HTML5, CSS3, JavaScript (ES6+)
- **Backend Framework**: Django (Python 3)
- **Database & Microservices**: Node.js, Express, MongoDB (Dealerships & Reviews Microservice)
- **Sentiment Analysis**: Microservice containerized for real-time review sentiment evaluation
- **Containerization & Deployment**: Docker, Kubernetes, GitHub Actions CI/CD pipeline

## Project Structure
- `server/djangoapp/`: Django application logic, views, models, and authentication endpoints.
- `server/frontend/`: React components and static assets (`About.html`, `Contact.html`).
- `server/database/`: Node.js Express microservices for Dealerships and Reviews.

## License
MIT License