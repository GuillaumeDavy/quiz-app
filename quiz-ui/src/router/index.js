import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsManager from '../views/QuestionsManager.vue'
import ScorePage from '../views/ScorePage.vue'
import AdminManager from '../views/AdminManager.vue'
import LoginPage from '../views/LoginPage.vue'
import localStorageService from '../services/LocalStorageService'
import quizApiService from '../Services/QuizApiService'

const router = createRouter({
    history: createWebHistory(
        import.meta.env.BASE_URL),
    routes: [{
            path: '/',
            name: 'HomePage',
            component: HomePage
        },
        {
            path: '/start-new-quiz-page',
            name: 'NewQuizPage',
            component: NewQuizPage
        },
        {
            path: '/questionsManager',
            name: 'QuestionsManager',
            component: QuestionsManager
        },
        {
            path: '/score',
            name: 'ScorePage',
            component: ScorePage
        },
        {
            path: '/admin',
            name: 'AdminManager',
            component: AdminManager
        },
        {
            path: '/login',
            name: 'LoginPage',
            component: LoginPage
        }
    ]
})

//secure admin page with token
router.beforeEach((to, from, next) => {
    if (to.name === 'AdminManager' && !localStorageService.getToken()) {
        next('/login')
    } else if (to.name !== 'AdminManager') {
        next()
    } else {
        if (localStorageService.getToken()) {
            let token = localStorageService.getToken()
                //console.log(token)
            quizApiService.isValidToken(token)
                .then(response => {
                    console.log(response)
                    if (response.data === 1) {
                        next()
                    } else {
                        next('/login')
                    }
                })
        }
    }
})

export default router