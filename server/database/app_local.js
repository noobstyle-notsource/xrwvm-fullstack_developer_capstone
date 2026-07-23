const express = require('express');
const fs = require('fs');
const cors = require('cors');
const path = require('path');

const app = express();
const port = 3030;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Load data from JSON files
const reviews_data = JSON.parse(fs.readFileSync(path.join(__dirname, 'data', 'reviews.json'), 'utf8'));
const dealerships_data = JSON.parse(fs.readFileSync(path.join(__dirname, 'data', 'dealerships.json'), 'utf8'));

let reviews = reviews_data['reviews'];
let dealerships = dealerships_data['dealerships'];

// Home
app.get('/', (req, res) => {
  res.send("Welcome to the Dealership API");
});

// Fetch all reviews
app.get('/fetchReviews', (req, res) => {
  res.json(reviews);
});

// Fetch reviews by dealer id
app.get('/fetchReviews/dealer/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const filtered = reviews.filter(r => r.dealership === id);
  res.json(filtered);
});

// Fetch all dealerships
app.get('/fetchDealers', (req, res) => {
  res.json(dealerships);
});

// Fetch dealers by state
app.get('/fetchDealers/:state', (req, res) => {
  const state = req.params.state;
  const filtered = dealerships.filter(d => d.state === state);
  res.json(filtered);
});

// Fetch dealer by id
app.get('/fetchDealer/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const filtered = dealerships.filter(d => d.id === id);
  res.json(filtered);
});

// Insert a review
app.post('/insert_review', (req, res) => {
  try {
    const data = req.body;
    const new_id = reviews.length > 0 ? Math.max(...reviews.map(r => r.id)) + 1 : 1;
    const review = {
      id: new_id,
      name: data.name,
      dealership: data.dealership,
      review: data.review,
      purchase: data.purchase,
      purchase_date: data.purchase_date,
      car_make: data.car_make,
      car_model: data.car_model,
      car_year: data.car_year,
    };
    reviews.push(review);
    res.json(review);
  } catch (error) {
    res.status(500).json({ error: 'Error inserting review' });
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
