<template>
  <div class="container mt-2">
    <div class="row">
      <div class="col-12">
        <h1 class="mb-3">Edit your answer</h1>
        <form @submit.prevent="onSubmit">
          <textarea v-model="answer_body" rows="3" class="form-control">
          </textarea>
          <br />
          <button type="submit" class="btn btn-sm btn-success">
            Send your answer
          </button>
        </form>
        <p class="error mt-2">{{ error }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service";

export default {
  name: "AnswerEditor",

  props: {
    id: {
      type: Number,
      required: true
    },
    answerEdit: {
      type: String,
      required: true
    },
    questionSlug: {
      type: String,
      required: true
    }
  },

  async beforeRouteEnter(to, from, next) {
    let endpoint = `/api/answers/${to.params.id}/`;
    await apiService(endpoint).then(data => {
      to.params.answerEdit = data.body;
      to.params.questionSlug = data.question_slug;
    });
    return next();
  },

  data() {
    return {
      answer_body: this.answerEdit,
      error: null
    };
  },

  methods: {
    onSubmit() {
      if (this.answer_body) {
        let endpoint = `/api/answers/${this.id}/`;
        apiService(endpoint, "PUT", { body: this.answer_body }).then(() => {
          this.$router.push({
            name: "question",
            params: { slug: this.questionSlug }
          });
        });
      } else {
        this.error = "The field cannot be empty!";
      }
    }
  }

  // methods: {
  //     async getAnswerData() {
  //         let endpoint = `/api/answers/${this.id}/`;
  //         await apiService(endpoint)
  //             .then(data => {
  //                 this.answer_body = data.body;
  //             })
  //     }

  // },
  // created() {
  //     this.getAnswerData();
  // }
};
</script>

<style></style>
