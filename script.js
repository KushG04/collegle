document.addEventListener('DOMContentLoaded', (event) => {
    var popupTriggers = document.querySelectorAll('.popup-trigger');
    var closeButton = document.getElementById('close-button');
    var popup = document.getElementById('popup');
    var overlay = document.getElementById('popup-overlay');
    var popupContent = document.getElementById('popup-content');
    var submitButton = document.getElementById('submit-guess');
    var guessInput = document.getElementById('guess');
    const suggestionsContainer = document.querySelector('.suggestions');
    const guessesContainer = document.querySelector('.guesses-container');
    const guessHeadings = document.querySelector('.guess-headings');
    const guessesList = document.querySelector('.guesses-list');
    const guessCounter = document.getElementById('guess-counter');

    //POPUP
    popupTriggers.forEach(trigger => {
        trigger.addEventListener('click', function(event) {
            if (event.currentTarget.id === 'how-link') {
                popupContent.innerHTML = `
                    <p>How to Play</p>
                    <ol>
                        <li>Enter the name of a college in the search box.</li>
                        <li>Your guesses will appear below with details like ranking, type, state, and acceptance rate.</li>
                        <li>Use the clues provided by your guesses to deduce the correct college:</li>
                            <ol>
                                <li>If the ranking is displayed in orange, the correct ranking is within 10 spots.</li>
                                <li>If the state is displayed in orange, the correct state is a neighboring state.</li>
                                <li>If the acceptance rate is displayed in orange, the correct acceptance rate is within 10 percent.</li>
                            </ol>
                        <li>You have 7 tries to find the correct college!</li>
                    </ol>
                `;
            } else if (event.currentTarget.id === 'stats-link') {
                popupContent.innerHTML = `<p>Statistics</p><p>Wins: ${wins}</p><p>Losses: ${losses}</p>`;
            }
            overlay.classList.add('active');
            popup.classList.add('active');
        });
    });

    function showPopup(message) {
        popupContent.innerHTML = message;
        overlay.classList.add('active');
        popup.classList.add('active');

        window.onclick = function(event) {
            if (event.target == overlay || event.target == closeButton) {
                overlay.classList.remove('active');
                popup.classList.remove('active');
                resetGame();
            }
        }
    }

    closeButton.onclick = function() {
        overlay.classList.remove('active');
        popup.classList.remove('active');
    }

    window.onclick = function(event) {
        if (event.target == overlay) {
            overlay.classList.remove('active');
            popup.classList.remove('active');
        }
    }

    //CLEAR SEARCH
    submitButton.addEventListener('click', function() {
        hideSuggestions()
        checkGuess();
        guessInput.value = '';
    });

    guessInput.addEventListener('keyup', function(event) {
        if (event.key === 'Enter' && suggestionsContainer.style.display !== 'block') {
            hideSuggestions();
            checkGuess();
            guessInput.value = '';
        }
    });

    function hideSuggestions() {
        suggestionsContainer.innerHTML = "";
        suggestionsContainer.style.display = 'none';
        
    }

    //SEARCH SUGGESTIONS
    let colleges = {};
    let activeSuggestionIndex = -1;

    fetch('http://127.0.0.1:5502/colleges.json')
        .then(response => response.json())
        .then(data => {
            colleges = data;
            resetGame();
        })
        .catch(error => console.error('error loading colleges data: ', error));

    guessInput.addEventListener("input", function () {
        const query = guessInput.value.toLowerCase();
        console.log('user input: ', query);
        const filteredColleges = Object.keys(colleges).filter(collegeName =>
            collegeName.toLowerCase().includes(query)
        ).slice(0, 3);
        console.log('filtered colleges: ', filteredColleges);

        suggestionsContainer.innerHTML = "";
        activeSuggestionIndex = -1;
        
        if (query && filteredColleges.length > 0) {
            filteredColleges.forEach(collegeName => {
                const suggestionItem = document.createElement("div");
                suggestionItem.classList.add("suggestion-item");
                suggestionItem.textContent = collegeName;
                suggestionsContainer.appendChild(suggestionItem);
                suggestionItem.addEventListener("click", () => {
                    guessInput.value = collegeName;
                    suggestionsContainer.innerHTML = "";
                    suggestionsContainer.style.display = 'none';
                    activeSuggestionIndex = -1;
                });
            });
            suggestionsContainer.style.display = 'block';
        } else {
            suggestionsContainer.style.display = 'none';
        }
    });

    guessInput.addEventListener("keydown", function (event) {
        const suggestions = document.querySelectorAll('.suggestion-item');
        if (suggestions.length > 0) {
            if (event.key === "ArrowDown") {
                activeSuggestionIndex = (activeSuggestionIndex + 1) % suggestions.length;
                updateActiveSuggestion(suggestions);
                event.preventDefault();
            } else if (event.key === "ArrowUp") {
                activeSuggestionIndex = (activeSuggestionIndex - 1 + suggestions.length) % suggestions.length;
                updateActiveSuggestion(suggestions);
                event.preventDefault();
            } else if (event.key === "Enter") {
                if (activeSuggestionIndex >= 0 && activeSuggestionIndex < suggestions.length) {
                    guessInput.value = suggestions[activeSuggestionIndex].textContent;
                    suggestionsContainer.innerHTML = "";
                    suggestionsContainer.style.display = 'none';
                    activeSuggestionIndex = -1;
                    event.preventDefault();
                }
            }
        }
    });

    function updateActiveSuggestion(suggestions) {
        suggestions.forEach((suggestion, index) => {
            suggestion.classList.toggle('active', index === activeSuggestionIndex);
        });
    }

    //GUESSES
    function addGuess() {
        const guessValue = guessInput.value.trim();
        if (!guessValue) return;
        if (colleges[guessValue]) {
            const collegeData = colleges[guessValue];
            const correctData = colleges[correctCollege];

            const guessItem = document.createElement('div');
            guessItem.classList.add('guess-item');

            const nameColor = guessValue === correctCollege ? 'green' : 'black';
            const rankColor = guessRankColor(collegeData.ranking, correctData.ranking);
            const typeColor = collegeData.type === correctData.type ? 'green' : 'black';
            const stateColor = guessStateColor(collegeData.state, correctData.state);
            const rateColor = guessRateColor(collegeData.acceptance_rate, correctData.acceptance_rate);

            guessItem.innerHTML = `
                <div style="color: ${nameColor};">${guessValue}</div>
                <div style="color: ${rankColor};">${collegeData.ranking}</div>
                <div style="color: ${typeColor};">${collegeData.type}</div>
                <div style="color: ${stateColor};">${collegeData.state}</div>
                <div style="color: ${rateColor};">${collegeData.acceptance_rate}</div>
            `;
            guessesList.appendChild(guessItem);
            guessHeadings.style.display = 'grid';
        }
    }

    //CLUES
    const neighboringStates = {
        "AL": ["FL", "GA", "MS", "TN"],
        "AK": [],
        "AZ": ["CA", "CO", "NV", "NM", "UT"],
        "AR": ["LA", "MO", "MS", "OK", "TN", "TX"],
        "CA": ["AZ", "NV", "OR"],
        "CO": ["AZ", "KS", "NE", "NM", "OK", "UT", "WY"],
        "CT": ["MA", "NY", "RI"],
        "DE": ["MD", "NJ", "PA"],
        "FL": ["AL", "GA"],
        "GA": ["AL", "FL", "NC", "SC", "TN"],
        "HI": [],
        "ID": ["MT", "NV", "OR", "UT", "WA", "WY"],
        "IL": ["IA", "IN", "KY", "MO", "WI"],
        "IN": ["IL", "KY", "MI", "OH"],
        "IA": ["IL", "MN", "MO", "NE", "SD", "WI"],
        "KS": ["CO", "MO", "NE", "OK"],
        "KY": ["IL", "IN", "MO", "OH", "TN", "VA", "WV"],
        "LA": ["AR", "MS", "TX"],
        "ME": ["NH"],
        "MD": ["DE", "PA", "VA", "WV"],
        "MA": ["CT", "NH", "NY", "RI", "VT"],
        "MI": ["IN", "OH", "WI"],
        "MN": ["IA", "ND", "SD", "WI"],
        "MS": ["AL", "AR", "LA", "TN"],
        "MO": ["AR", "IL", "IA", "KS", "KY", "NE", "OK", "TN"],
        "MT": ["ID", "ND", "SD", "WY"],
        "NE": ["CO", "IA", "KS", "MO", "SD", "WY"],
        "NV": ["AZ", "CA", "ID", "OR", "UT"],
        "NH": ["MA", "ME", "VT"],
        "NJ": ["DE", "NY", "PA"],
        "NM": ["AZ", "CO", "OK", "TX", "UT"],
        "NY": ["CT", "MA", "NJ", "PA", "VT"],
        "NC": ["GA", "SC", "TN", "VA"],
        "ND": ["MN", "MT", "SD"],
        "OH": ["IN", "KY", "MI", "PA", "WV"],
        "OK": ["AR", "CO", "KS", "MO", "NM", "TX"],
        "OR": ["CA", "ID", "NV", "WA"],
        "PA": ["DE", "MD", "NJ", "NY", "OH", "WV"],
        "RI": ["CT", "MA"],
        "SC": ["GA", "NC"],
        "SD": ["IA", "MN", "MT", "NE", "ND", "WY"],
        "TN": ["AL", "AR", "GA", "KY", "MO", "MS", "NC", "VA"],
        "TX": ["AR", "LA", "NM", "OK"],
        "UT": ["AZ", "CO", "ID", "NV", "WY"],
        "VT": ["MA", "NH", "NY"],
        "VA": ["KY", "MD", "NC", "TN", "WV"],
        "WA": ["ID", "OR"],
        "WV": ["KY", "MD", "OH", "PA", "VA"],
        "WI": ["IA", "IL", "MI", "MN"],
        "WY": ["CO", "ID", "MT", "NE", "SD", "UT"]
    };

    function guessRankColor(guessRank, correctRank) {
        if (guessRank === correctRank) {
            return 'green';
        } else if (Math.abs(guessRank - correctRank) <= 10) {
            return 'orange';
        } else {
            return 'black';
        }
    }

    function guessStateColor(guessState, correctState) {
        if (guessState === correctState) {
            return 'green';
        } else if (neighboringStates[correctState].includes(guessState)) {
            return 'orange';
        } else {
            return 'black';
        }
    }

    function guessRateColor(guessRate, correctRate) {
        if (guessRate === correctRate) {
            return 'green';
        } else if (Math.abs(guessRate - correctRate) <= 10) {
            return 'orange';
        } else {
            return 'black';
        }
    }

    //CHECKING GUESSES
    let correctCollege = '';
    let guesses = 0;
    let maxGuesses = 7;
    let wins = 0;
    let losses = 0;

    function resetGame() {
        correctCollege = getRandomCollege();
        guesses = 0;
        guessesList.innerHTML = '';
        guessCounter.textContent = 'Guess 0 of 7'
        guessInput.value = '';
    }

    function getRandomCollege() {
        const collegeNames = Object.keys(colleges);
        const randomIndex = Math.floor(Math.random() * collegeNames.length);
        return collegeNames[randomIndex];
    }

    function checkGuess() {
        const guessValue = guessInput.value.trim();
        if (!guessValue || !colleges[guessValue]) return;

        guesses++;
        guessCounter.textContent = `Guess ${guesses} of 7`;
        addGuess(guessValue);

        if (guessValue === correctCollege) {
            wins++;
            setTimeout(() => showPopup('<p>You Won!</p>'), 100);
        } else if (guesses >= maxGuesses) {
            losses++;
            setTimeout(() => showPopup(`<p>You Lost!</p><p>The correct college was ${correctCollege}.</p>`), 100);
        }
    }
});