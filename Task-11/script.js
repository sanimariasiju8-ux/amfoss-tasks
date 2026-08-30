// ================================
// NOOL — Interactive JavaScript
// ================================


// --------------------------------
// Kerala Region Data
// --------------------------------

const regionData = {

    "North Kerala": {
        title: "North Kerala",
        text: "A region rich with Theyyam, folk traditions, coastal stories and distinctive Malabar cuisine."
    },

    "Central Kerala": {
        title: "Central Kerala",
        text: "Explore temple traditions, classical art forms, historic trade routes and the cultural heartlands of Kerala."
    },

    "South Kerala": {
        title: "South Kerala",
        text: "Discover backwaters, traditional architecture, festivals, crafts and stories rooted in southern Kerala."
    }

};


// --------------------------------
// Show Selected Region
// --------------------------------

function showRegion(region) {

    const data = regionData[region];

    const info = document.getElementById("regionInfo");

    info.innerHTML = `
        <p class="small-label">YOU FOUND A THREAD</p>

        <h3>${data.title}</h3>

        <p>${data.text}</p>
    `;

}


// --------------------------------
// Culture Thread Data
// --------------------------------

const threadData = {

    "Art & Performance":
        "Explore Kerala's visual and performing traditions, from Kathakali and Mohiniyattam to Theyyam and Chenda.",

    "Food":
        "Discover the flavours, ingredients and family traditions behind Kerala's diverse food culture.",

    "Festivals":
        "Explore celebrations that bring families, villages and communities together.",

    "Stories & Folklore":
        "Uncover legends, folk tales and stories passed from one generation to another.",

    "Language":
        "Discover Malayalam words, expressions and the cultural meanings hidden inside everyday language.",

    "Heritage":
        "Explore historic places, architecture, crafts and traditions that shaped Kerala."

};


// --------------------------------
// Open Culture Thread
// --------------------------------

function openThread(thread) {

    document.getElementById("modalTitle").textContent = thread;

    document.getElementById("modalText").textContent =
        threadData[thread];

    document.getElementById("modal").classList.add("active");

}


// --------------------------------
// Close Modal
// --------------------------------

function closeModal() {

    document.getElementById("modal").classList.remove("active");

}


// --------------------------------
// Story Button
// --------------------------------

function readStory() {

    document.getElementById("modalTitle").textContent =
        "The rhythm of tradition";

    document.getElementById("modalText").textContent =
        "Kerala's traditions continue because people carry them forward — through performances, food, language, celebrations and stories. Nool is imagined as a place where these threads can be discovered and shared.";

    document.getElementById("modal").classList.add("active");

}


// --------------------------------
// Malayalam Word Collection
// --------------------------------

const words = [

    {
        malayalam: "ഓർമ്മ",
        english: "Ormma",
        meaning: "Memory"
    },

    {
        malayalam: "മഴ",
        english: "Mazha",
        meaning: "Rain"
    },

    {
        malayalam: "സ്നേഹം",
        english: "Sneham",
        meaning: "Affection"
    },

    {
        malayalam: "നിലാവ്",
        english: "Nilaavu",
        meaning: "Moonlight"
    }

];


let wordIndex = 0;


// --------------------------------
// Change Malayalam Word
// --------------------------------

function newWord() {

    wordIndex++;

    if (wordIndex >= words.length) {
        wordIndex = 0;
    }

    const word = words[wordIndex];

    document.querySelector(".malayalam").textContent =
        word.malayalam;

    document.querySelector(".word-card h3").textContent =
        word.english;

    document.querySelector(".meaning").textContent =
        `/ ${word.meaning} /`;

}


// --------------------------------
// Cultural Quiz
// --------------------------------

function checkAnswer(answer) {

    const result = document.getElementById("quizResult");

    if (answer === "North Kerala") {

        result.textContent =
            "✓ Correct! Theyyyam has deep roots in North Kerala.";

        result.style.color = "#28594d";

    } else {

        result.textContent =
            "Not quite — try another thread.";

        result.style.color = "#c56b43";

    }

}


// --------------------------------
// Mobile Navigation
// --------------------------------

function toggleMenu() {

    const nav = document.querySelector(".navbar nav");

    if (nav.style.display === "flex") {

        nav.style.display = "none";

    } else {

        nav.style.display = "flex";

        nav.style.flexDirection = "column";

        nav.style.position = "absolute";

        nav.style.top = "76px";

        nav.style.right = "5%";

        nav.style.background = "#fffaf1";

        nav.style.padding = "20px";

        nav.style.border = "1px solid #ddd3c2";

    }

}


// --------------------------------
// Close Modal by Clicking Outside
// --------------------------------

document.getElementById("modal").addEventListener(
    "click",
    function(event) {

        if (event.target === this) {
            closeModal();
        }

    }
);