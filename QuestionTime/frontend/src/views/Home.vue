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
						<h5 class="card-title">
							<router-link 
								:to="{name: 'question', params:{slug: question.slug} }"
								class="question-link"
								>{{ question.content }}
							</router-link>
						</h5>
						<hr class="mb-1 mt-1">
						<p class="card-text answers-count">Answers: {{ question.answers_count}}</p>
					</div>
				</div>
			</div>
			<div class="my-4">
				<div v-show="loadingQuestions" 
					 class="spinner-border text-success" 
					 role="status">
  					<span class="sr-only">Loading...</span>
				</div>
				<button v-show="next" 
						@click="getQuestions" 
						class="btn btn-sm btn-outline-success"
					>Load another questions
				</button>
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
	  questions: [],
	  next: null,
	  loadingQuestions: false
    }
  },

  methods: {
    getQuestions() {
	  let endpoint = "/api/questions/";
	  if (this.next) {
		  endpoint = this.next;
	  }
	  this.loadingQuestions = true;
      apiService(endpoint)
        .then(data => {
		  this.questions.push(...data.results);
		  this.loadingQuestions = false;
		  if (data.next) {
			  this.next = data.next;
		  } else {
			  this.next = null;
		  }
        })
    }
  },

  created() {
	this.getQuestions();
	document.title = "QuestionTime";
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

	.card-header {
		font-size: 80%;
	}

	.question-link {
		font-weight: bold;
		color: black;
	}

	.question-link:hover {
		color: #343A40;
		text-decoration: none;
	}
</style>

