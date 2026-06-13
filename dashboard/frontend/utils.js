// ==========================================
// SecureWatch AI
// utils.js
// ==========================================

const API = window.location.origin;

// ------------------------------------------
// Set Text Content
// ------------------------------------------

function setValue(id, value) {

    const element = document.getElementById(id);

    if (element) {

        element.textContent = value ?? "--";

    }

}

// ------------------------------------------
// Set HTML
// ------------------------------------------

function setHTML(id, value) {

    const element = document.getElementById(id);

    if (element) {

        element.innerHTML = value ?? "";

    }

}

// ------------------------------------------
// Create Info Row
// ------------------------------------------

function createRow(label, value) {

    return `

        <div class="info-row">

            <span class="label">

                ${label}

            </span>

            <span class="value">

                ${value ?? "--"}

            </span>

        </div>

    `;

}

// ------------------------------------------
// Get JSON
// ------------------------------------------

async function getJSON(url) {

    const response = await fetch(url);

    if (!response.ok) {

        throw new Error(

            `HTTP ${response.status}`

        );

    }

    return await response.json();

}

// ------------------------------------------
// POST Request
// ------------------------------------------

async function postJSON(url, body = {}) {

    const response = await fetch(

        url,

        {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(body)

        }

    );

    if (!response.ok) {

        throw new Error(

            `HTTP ${response.status}`

        );

    }

    return await response.json();

}

// ------------------------------------------
// Format Date & Time
// ------------------------------------------

function formatDate(dateString) {

    if (!dateString) {

        return "--";

    }

    return new Date(

        dateString

    ).toLocaleString();

}

// ------------------------------------------
// Delay Helper
// ------------------------------------------

function sleep(ms) {

    return new Promise(

        resolve => setTimeout(

            resolve,

            ms

        )

    );

}

// ------------------------------------------
// Element Shortcut
// ------------------------------------------

function $(id) {

    return document.getElementById(id);

}

// ------------------------------------------
// Query Shortcut
// ------------------------------------------

function $$(selector) {

    return document.querySelectorAll(selector);

}

// ------------------------------------------
// Console Banner
// ------------------------------------------

console.log(

    "%c🛡 SecureWatch AI Utils Loaded",

    "color:#4CAF50;font-size:15px;font-weight:bold;"

);