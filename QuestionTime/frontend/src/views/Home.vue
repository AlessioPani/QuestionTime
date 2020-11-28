<template>
<div class="home-view">
    <div class="container"> 
        <div class="mt-2">
        	<div v-for="question in questions" :key="question.pk">
				<div class="card border-secondary mt-2">
					<div class="card-header">
						Question submitted by 
						<span class="author-name">{{ question.author }}</span>
						on
						<span class="created-date">{{ question.created_at }}</span>
					</div>
					<div class="card-body">
						<h5 class="card-title">{{ question.content }}</h5>
						<hr class="mb-1 mt-1">
						<p class="card-text answers-count">Answers: {{ question.answers_count}}</p>
					</div>
				</div>
			</div>
        </div>
    </div>
</div>
</template>

<script>
import { apiService } from "../common/api.service"

export default {
  name: "Home",

  data() {
    return {
      questions: []
    }
  },

  methods: {
    getQuestions() {
      let endpoint = "/api/questions/";
      apiService(endpoint)
        .then(data => {
          this.questions.push(...data.results)
        })
    }
  },

  created() {
    this.getQuestions();
  }
};
</script>

<style media="screen">
	.author-name {
		font-weight: bold;
		color: #DC3545;
	}

	.answers-count {
		font-size: 80%;
	}

	.created-date {
		font-weight: bold;
		color: #DC3545;
	}
</style>

