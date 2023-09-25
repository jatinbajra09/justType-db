
    // Initialize unlocked levels (Level 1 is unlocked by default).
    let unlockedLevels = 1;

    // Function to display an error message.
    function displayError(message) {
        alert(message);
    }

    // Function to check if the user is allowed to access a level.
    function checkAccess(level) {
        if (level <= unlockedLevels) {
            // User is allowed to access the level.
            return true;
        } else {
            // User is not allowed to access the level.
            displayError("You must complete the current level first.");
            return false;
        }
    }

    // Function to unlock the next level (e.g., Level 2) based on user performance.
    function unlockNextLevel(speed, accuracy) {
        if (unlockedLevels === 1 && speed >= 42 && accuracy >= 81) {
            unlockedLevels = 2;
            alert("Congratulations! Level 2 is now unlocked.");
            // Redirect the user to Level 2 (replace "level2.html" with your actual path).
            window.location.href = "good typing/easylev2.html"; // Adjust the path as needed.
        }
    }

    
    document.getElementById("level1").addEventListener("click", function (e) {
        // Prompt the user to enter their actual speed (WPM) and accuracy (%) after the test.
        const userSpeed = parseFloat(prompt("Enter your WPM (Words Per Minute):"));
        const userAccuracy = parseFloat(prompt("Enter your accuracy (%):"));
        
        if (!isNaN(userSpeed) && !isNaN(userAccuracy) && userSpeed >= 42 && userAccuracy >= 81) {
            // Call unlockNextLevel with the actual user performance values.
            unlockNextLevel(userSpeed, userAccuracy);
        } else {
            alert("Please enter valid speed and accuracy values.");
            e.preventDefault(); // Prevent the link from being followed if the values are not provided or are invalid.
        }
    });

    // Add event listeners to level links.
    document.getElementById("level1").addEventListener("click", function (e) {
        // User is allowed to access Level 1.
    });

    document.getElementById("level2").addEventListener("click", function (e) {
        // Check if the user is allowed to access Level 2.
        if (!checkAccess(2)) {
            e.preventDefault(); // Prevent the link from being followed.
        }
    });

    document.getElementById("level3").addEventListener("click", function (e) {
        // Check if the user is allowed to access Level 3.
        if (!checkAccess(3)) {
            e.preventDefault(); // Prevent the link from being followed.
        }
    });

    document.getElementById("level4").addEventListener("click", function (e) {
        // Check if the user is allowed to access Level 4.
        if (!checkAccess(4)) {
            e.preventDefault(); // Prevent the link from being followed.
        }
    });

    document.getElementById("level5").addEventListener("click", function (e) {
        // Check if the user is allowed to access Level 5.
        if (!checkAccess(5)) {
            e.preventDefault(); // Prevent the link from being followed.
        }
    });