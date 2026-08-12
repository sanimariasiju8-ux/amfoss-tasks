const coinName = document.getElementById("coinName");
const coinSymbol = document.getElementById("coinSymbol");
const coinPrice = document.getElementById("coinPrice");
const coinChange = document.getElementById("coinChange");

const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");
const themeToggle = document.getElementById("themeToggle");
const wishlistButton =
    document.getElementById("wishlistButton");

const wishlistContainer =
    document.getElementById("wishlist");

let wishlist =
    JSON.parse(localStorage.getItem("cryptoWishlist")) || [];

const API_URL =
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=25&page=1&sparkline=false";

let coins = [];
let currentCoin = null;
let priceChart = null;


// Load the top 25 cryptocurrencies
async function loadCoins() {
    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }

        coins = await response.json();

        displayCoin(coins[0]);

    } catch (error) {
        console.error("Failed to load coins:", error);
        coinName.textContent = "Unable to load data";
    }
}


// Display selected coin
function displayCoin(coin) {

    if (!coin) return;

    currentCoin = coin;

    coinName.textContent = coin.name;
    coinSymbol.textContent = coin.symbol.toUpperCase();

    coinPrice.textContent =
        "$" + Number(coin.current_price).toLocaleString();

    coinChange.textContent =
        Number(coin.price_change_percentage_24h || 0).toFixed(2) + "%";

    // Load default 24-hour chart
    getChartData(coin.id, 1);
}


// Search cryptocurrency
searchButton.addEventListener("click", () => {

    const searchTerm = searchInput.value.trim().toLowerCase();

    if (!searchTerm) return;

    const coin = coins.find(
        coin =>
            coin.name.toLowerCase() === searchTerm ||
            coin.symbol.toLowerCase() === searchTerm
    );

    if (coin) {
        displayCoin(coin);
    } else {
        coinName.textContent = "Coin not found";
        coinSymbol.textContent = "";
        coinPrice.textContent = "$0.00";
        coinChange.textContent = "0.00%";
    }
});


searchInput.addEventListener("keypress", event => {

    if (event.key === "Enter") {
        searchButton.click();
    }

});


// Get historical price data
async function getChartData(coinId, days) {

    try {

        const response = await fetch(
            `https://api.coingecko.com/api/v3/coins/${coinId}/market_chart?vs_currency=usd&days=${days}`
        );

        if (!response.ok) {
            throw new Error(`Chart API error: ${response.status}`);
        }

        const data = await response.json();

        const prices = data.prices;

        const labels = prices.map(price => {

            const date = new Date(price[0]);

            return date.toLocaleString([], {
                month: "short",
                day: "numeric",
                hour: "2-digit",
                minute: "2-digit"
            });

        });

        const priceValues = prices.map(price => price[1]);

        createChart(labels, priceValues);

    } catch (error) {

        console.error("Chart error:", error);

    }
}


// Create Chart.js graph
function createChart(labels, prices) {

    const ctx = document
        .getElementById("priceChart")
        .getContext("2d");

    if (priceChart) {
        priceChart.destroy();
    }

    priceChart = new Chart(ctx, {

        type: "line",

        data: {

            labels: labels,

            datasets: [{
                label: "Price (USD)",
                data: prices,
                borderWidth: 2,
                tension: 0.3,
                pointRadius: 0,
                fill: false
            }]

        },

        options: {

            responsive: true,
            maintainAspectRatio: false,

            plugins: {

                legend: {
                    display: true
                }

            },

            scales: {

                x: {
                    display: true
                },

                y: {
                    beginAtZero: false
                }

            }

        }

    });

}


// Time-range buttons
const timeButtons =
    document.querySelectorAll(".time-buttons button");

timeButtons.forEach(button => {

    button.addEventListener("click", () => {

        if (!currentCoin) return;

        const days = button.dataset.days;

        getChartData(currentCoin.id, days);

    });

});

wishlistButton.addEventListener("click", () => {

    if (!currentCoin) return;

    const alreadyAdded = wishlist.some(
        coin => coin.id === currentCoin.id
    );

    if (!alreadyAdded) {
        wishlist.push(currentCoin);

        localStorage.setItem("cryptoWishlist",JSON.stringify(wishlist)
    )
        displayWishlist();
    }

});


function displayWishlist() {

    wishlistContainer.innerHTML = "";

    if (wishlist.length === 0) {

        wishlistContainer.innerHTML =
            "<p>No cryptocurrencies added yet.</p>";

        return;
    }

    wishlist.forEach(coin => {

        const item = document.createElement("div");

        item.className = "wishlist-item";

        item.innerHTML = `
            <span>
                ⭐ ${coin.name}
                (${coin.symbol.toUpperCase()})
            </span>

            <button class="remove-wishlist">
                Remove
            </button>
        `;

        item.querySelector(".remove-wishlist")
            .addEventListener("click", () => {

                wishlist = wishlist.filter(
                    item => item.id !== coin.id
                );

                localStorage.setItem("cryptoWishlist",JSON.stringify(wishlist))

                displayWishlist();

            });

        wishlistContainer.appendChild(item);

    });
}

themeToggle.addEventListener("click", () => {

    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {

        themeToggle.textContent = "☀️ Light Mode";

        localStorage.setItem("theme", "dark");

    } else {

        themeToggle.textContent = "🌙 Dark Mode";

        localStorage.setItem("theme", "light");

    }

});
const savedTheme = localStorage.getItem("theme");

if (savedTheme === "dark") {

    document.body.classList.add("dark-mode");

    themeToggle.textContent = "☀️ Light Mode";

}



// Start application
loadCoins();
displayWishlist();