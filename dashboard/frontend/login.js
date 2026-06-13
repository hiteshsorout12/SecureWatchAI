// ==========================================
// SecureWatch AI
// login.js
// ==========================================

const API = window.location.origin;

// ==========================================
// Startup
// ==========================================

window.onload = () => {

    checkLogin();

    document
        .getElementById("loginForm")
        .addEventListener(
            "submit",
            login
        );

};

// ==========================================
// Login
// ==========================================

async function login(event) {

    event.preventDefault();

    const username = document
        .getElementById(
            "username"
        ).value.trim();

    const password = document
        .getElementById(
            "password"
        ).value;

    if (!username || !password) {

        setStatus(

            "Enter username and password",

            "red"

        );

        return;

    }

    try {

        const response = await fetch(

            `${API}/login`,

            {

                method: "POST",

                headers: {

                    "Content-Type":
                        "application/json"

                },

                body: JSON.stringify({

                    username,

                    password

                })

            }

        );

        const data = await response.json();

        if (data.success) {

            localStorage.setItem(

                "securewatch_token",

                data.token

            );

            localStorage.setItem(

                "securewatch_user",

                username

            );

            setStatus(

                "Login Successful",

                "#00c853"

            );

            setTimeout(() => {

                window.location = "/";

            }, 1000);

        }

        else {

            setStatus(

                data.message ||

                "Invalid Credentials",

                "#ef4444"

            );

        }

    }

    catch (e) {

        console.error(e);

        setStatus(

            "Server Error",

            "#ef4444"

        );

    }

}

// ==========================================
// Logout
// ==========================================

function logout() {

    localStorage.removeItem(

        "securewatch_token"

    );

    localStorage.removeItem(

        "securewatch_user"

    );

    window.location = "/login";

}

// ==========================================
// Check Login
// ==========================================

function checkLogin() {

    const token =

        localStorage.getItem(

            "securewatch_token"

        );

    if (

        token &&

        window.location.pathname ===

        "/login"

    ) {

        window.location = "/";

    }

}

// ==========================================
// Authentication Header
// ==========================================

function authHeaders() {

    return {

        "Authorization":

            "Bearer " +

            localStorage.getItem(

                "securewatch_token"

            )

    };

}

// ==========================================
// Session Expiry
// ==========================================

function sessionExpired() {

    alert(

        "Session Expired"

    );

    logout();

}

// ==========================================
// Status
// ==========================================

function setStatus(

    message,

    color

) {

    const status =

        document.getElementById(

            "loginStatus"

        );

    status.innerHTML = message;

    status.style.color = color;

}

// ==========================================
// Enter Key
// ==========================================

document.addEventListener(

    "keypress",

    function (e) {

        if (

            e.key === "Enter"

        ) {

            document

                .querySelector(

                    "button"

                )

                .click();

        }

    }

);

// ==========================================
// Console
// ==========================================

console.log(

    "%c🔐 Login Module Loaded",

    "color:#4CAF50;font-size:14px;font-weight:bold"

);