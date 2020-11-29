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
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service"

export default {
    name: "Question",

    props: {
        slug: {
            type: String,
            required: true
        }
    },

    data() {
        return {
            question: {}
        }
    },

    methods: {
        getQuestionData() {
            let endpoint = `/api/questions/${this.slug}/`;
            apiService(endpoint)
                .then(data => {
                    this.question = data;
                    this.setPageTitle(data.content);
                })
        },

        setPageTitle(title) {
            document.title = title;
        }
    },

    created() {
        this.getQuestionData();
    }
}
</script>

<style media="screen">
    .question-content {
        font-size: 150%;
    }
</style>