export default {
    clear() {
        //toDo
    },
    savePlayerName(playerName) {
        window.localStorage.setItem("playerName", playerName);
    },
    getPlayerName() {
        return window.localStorage.getItem("playerName");
    },
    saveParticipationScore(participationScore) {
        window.localStorage.setItem("participationScore", participationScore);
    },
    getParticipationScore() {
        return window.localStorage.getItem("participationScore");
    },
    saveQuestionSize(questionSize) {
        window.localStorage.setItem("questionSize", questionSize);
    },
    getQuestionSize() {
        return window.localStorage.getItem("questionSize");
    }
};