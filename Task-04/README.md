# The Bull & The Bear — Crypto Tracker

A responsive cryptocurrency tracking web application built using **HTML, CSS, and JavaScript**. The application uses live cryptocurrency data from the **CoinGecko API** to help users search, monitor, and explore cryptocurrency prices and trends in one place.

## About the Project

Keeping track of cryptocurrency markets can be difficult because prices change constantly. This project brings important cryptocurrency information together in a simple and user-friendly interface.

Users can search for cryptocurrencies, view their current prices and market information, analyze price trends using interactive charts, and save their favorite cryptocurrencies to a wishlist.

## Features

- **Cryptocurrency Search**
  - Search for cryptocurrencies by name.
  - Quickly find the required cryptocurrency from the available market data.

- **Live Cryptocurrency Prices**
  - Displays current cryptocurrency prices.
  - Shows market-related information obtained from the CoinGecko API.

- **Interactive Price Charts**
  - Uses Chart.js to visualize cryptocurrency price history.
  - Supports multiple time ranges such as:
    - 24 Hours
    - 1 Week
    - 1 Month
    - 3 Months
    - 1 Year

- **Wishlist**
  - Add cryptocurrencies to a personal wishlist.
  - Remove cryptocurrencies when they are no longer needed.
  - Wishlist data is stored using `localStorage`, so it remains available after refreshing the page.

- **Dark / Light Mode**
  - Switch between light and dark themes.
  - The selected theme is remembered using `localStorage`.

- **Responsive Design**
  - Designed to work across different screen sizes.
  - Uses CSS to provide a clean and accessible layout.

## Technologies Used

- **HTML5** — Structure of the webpage
- **CSS3** — Styling, layout, responsiveness, and themes
- **JavaScript** — Application logic and API interaction
- **CoinGecko API** — Live cryptocurrency market data
- **Chart.js** — Interactive price charts
- **LocalStorage** — Saving wishlist and theme preferences

##  API Used

This project uses the **CoinGecko API** to retrieve cryptocurrency market information and historical price data.

Main market endpoint:
https://api.coingecko.com/api/v3/coins/markets

## Project Structure

**index.html**
Contains the structure of the Crypto Tracker, including:
Header
Search section
Cryptocurrency information
Price chart
Time-range buttons
Wishlist section
Theme toggle

**style.css**
Handles:
Page layout
Cards and buttons
Responsive design
Light mode
Dark mode
Chart and wishlist styling

**script.js**
Handles the main functionality of the application:
Fetching data from the CoinGecko API
Searching cryptocurrencies
Displaying market information
Creating and updating charts
Changing chart time ranges
Managing the wishlist
Saving data using localStorage
Switching between dark and light themes

## Concepts Learned
Through this task, I learned and practiced:
1. Working with APIs
I learned how web applications can communicate with external APIs and use live data instead of displaying only static information.
2. Fetch API
JavaScript's fetch() was used to request cryptocurrency data from CoinGecko.
3. JSON Data
I learned how API responses are returned as JSON and how JavaScript can extract the required information from the response.
4. Async/Await
I learned how async and await make asynchronous API operations easier to write and understand.
5. DOM Manipulation
I learned how JavaScript can dynamically create and update HTML elements based on API data and user actions.
6. Event Handling
I used event listeners to respond to actions such as:
Searching
Clicking time-range buttons
Adding/removing wishlist items
Changing the theme
7. Chart.js
I learned how to use a JavaScript library to create interactive charts and represent changing cryptocurrency prices visually.
8. LocalStorage
I learned how browser localStorage can be used to save small amounts of user data so that preferences remain after refreshing the webpage.
9. Responsive Web Design
I learned how CSS media queries and flexible layouts can make a website usable on different screen sizes.
10. Error Handling
I learned that API requests can fail and that applications should provide meaningful feedback instead of leaving the user with a blank screen.

## 🌍 Deployed Project

[View the Live Crypto Tracker](https://amfoss-tasks-sandy.vercel.app/)
