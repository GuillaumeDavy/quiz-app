import axios from "axios";
import localStorageService from "./LocalStorageService";

const instance = axios.create({
    baseURL: `${import.meta.env.VITE_API_URL}`,
    json: true
});

export default {
    async call(method, resource, data = null, token = null) {
        var headers = {
            "Content-Type": "application/json",
        };
        if (token != null) {
            headers.authorization = "Bearer " + token;
        }

        return instance({
                method,
                headers: headers,
                url: resource,
                data,
            })
            .then((response) => {
                return { status: response.status, data: response.data };
            })
            .catch((error) => {
                return { status: error.response.status, data: error.response.data };
            });
    },
    getQuizInfo() {
        return this.call("get", "quiz-info");
    },
    getQuestion(position) {
        return this.call("get", `questions/${position}`);
    },
    getQuestions() {
        return this.call("get", "questions");
    },
    submitParticipation(playerName, answers) {
        return this.call("post", `participations`, {
            playerName: playerName,
            answers: answers
        });
    },
    login(password) {
        return this.call("post", "login", {
            password: password
        });
    },
    isValidToken(token) {
        console.log(token)
        return this.call("post", `check-token`, {
            token: token
        });
    }
};