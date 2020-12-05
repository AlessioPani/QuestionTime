<template>
    <div class="single-question mt-2">
        <div class="container">
             <div class="card border-secondary mt-2">
				<div class="card-header">
						Question submitted by 
						<span class="author-name">{{ question.author }}</span>
						on
						<span class="created-date">{{ question.created_at }}</span>
				</div>
				<div class="card-body">
					<h5 class="card-title question-content"> {{ question.content }} </h5>
					<hr class="mb-1 mt-1">
					<p class="card-text answers-count">Answers: {{ question.answers_count}}</p>
				</div>
			</div>
            <hr>
            <template v-if="userHasAnswered">
                <p class="answer-added">You've already answered this question!</p>
            </template>
            <template v-else-if="showForm">
                <form class="card" @submit.prevent="onSubmit">
                    <div class="card-header px-3">
                        Add an answer
                    </div>
                    <div class="card-body">
                        <textarea v-model="newAnswerBody"
                                  class="form-control" 
                                  rows="5" 
                                  placeholder="Add your answer.">
                        </textarea>
                    </div>
                    <div class="card-footer">
                        <button class="btn btn-sm btn-success"
                                type="submit" 
                        >Add</button>
                    </div>
                </form>
                <p class="error mt-2">{{ error }}</p>
            </template>
            <template v-else>
                <button class="btn btn-sm btn-success"
                        @click="showForm = true">
                    Answer
                </button>
            </template>

            <hr>
            <AnswerComponent
                v-for="(answer, index) in answers"
                :answer="answer"
                :key="index"
            />
            <div class="my-4">
                <p v-show="loadingAnswers">...loading...</p>
                <button v-show="next" @click="getQuestionAnswers" class="btn btn-sm btn-success">
                    Load new answers
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service";
import AnswerComponent from "../components/Answer.vue";

export default {
    name: "Question",

    props: {
        slug: {
            type: String,
            required: true
        }
    },

    components: {
        AnswerComponent
    },

    data() {
        return {
            question: {},
            answers: [],
            loadingAnswers: false,
            userHasAnswered: false,
            showForm: false,
            newAnswerBody: null,
            error: null,
            next: null,
        }
    },

    methods: {
        getQuestionData() {
            let endpoint = `/api/questions/${this.slug}/`;
            apiService(endpoint)
                .then(data => {
                    this.question = data;
                    this.userHasAnswered = data.user_has_answered;
                    this.setPageTitle(data.content);
                })
        },

        setPageTitle(title) {
            document.title = title;
        },

        getQuestionAnswers() {
            let endpoint = `/api/questions/${this.slug}/answers/`;
            if (this.next) {
		        endpoint = this.next;
	        }
            this.loadingAnswers = true;
            apiService(endpoint)
                .then(data => {
                    this.answers.push(...data.results);
                    this.loadingAnswers = false;
                    if (data.next) {
                        this.next = data.next;
                    } else {
                        this.next = null;
                    }
                })
        },

        onSubmit() {
            if (this.newAnswerBody) {
                let endpoint = `/api/questions/${this.slug}/answer/`;
                apiService(endpoint, "POST", {body: this.newAnswerBody })
                    .then(data => {
                        this.answers.unshift(data);
                    })
                
                this.newAnswerBody = null;
                this.showForm = false;
                this.userHasAnswered = true;

                if (this.error) {
                    this.error = null;
                }
            } else {
                this.error = "Please, fill all the fields!";
            }
        },
    },

    created() {
        this.getQuestionData();
        this.getQuestionAnswers();
    }
}
</script>

<style lang="css">
    .question-content {
        font-size: 150%;
    }

    .answer-added {
        color: green;
        font-weight: bold;
    }

    .error {
        color: red;
        font-weight: bold;
    }
</style>