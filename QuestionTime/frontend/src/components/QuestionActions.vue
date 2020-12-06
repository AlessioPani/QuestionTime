<template>
  <div class="question-actions">
    <router-link
      :to="{ name: 'question-editor', params: { slug: slug } }"
      class="btn btn-sm btn-secondary mr-1"
      ><span>Edit</span>
    </router-link>
    <button class="btn btn-sm btn-danger" @click="deleteQuestion">
      Delete
    </button>
  </div>
</template>

<script>
import { apiService } from "../common/api.service";

export default {
  name: "QuestionActions",

  props: {
    slug: {
      type: String,
      required: true
    }
  },

  methods: {
    async deleteQuestion() {
      let endpoint = `/api/questions/${this.slug}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.$router.push({ name: "home" });
      } catch (error) {
        console.log(error);
      }
    }
  }
};
</script>

<style></style>
