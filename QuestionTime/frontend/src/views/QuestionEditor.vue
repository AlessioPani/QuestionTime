<template>
    <div class="container mt-2">
        <div class="row">
            <div class="col-12">
                <h1 class="mb-3">Add a question</h1>
                <form @submit.prevent="onSubmit">
                    <textarea 
                        v-model="question_body"
                        rows="3"
                        class="form-control"
                        placeholder="What do you wanna ask to our community?">
                    </textarea>
                    <br>
                    <button type="submit"
                            class="btn btn-sm btn-success"
                        >Send you question
                    </button>
                </form>
                <p class="muted error mt-2">{{ error }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service"

export default {
    name: "QuestionEditor",

    data() {
        return {
            question_body: null,
            error: null
        }
    },

    methods: {
        onSubmit() {
            if (!this.question_body) {
                this.error = "Question field must be filled!"
            } else if (this.question_body.length > 240) {
                this.error = "Maximum length of the question field is 240!"
            } else {
                let endpoint = "/api/questions/";
                let method = "POST";
                apiService(endpoint, method, {content: this.question_body})
                    .then(question_data => {
                        this.$router.push({
                            name: "question",
                            params: { slug: question_data.slug }
                        });
                    });
            }
        }
    },

    created() {
        document.title = "QuestionTime - Editor";
    }
}
</script>

<style>

</style>