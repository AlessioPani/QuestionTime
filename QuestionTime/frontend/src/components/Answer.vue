<template lang="html">
<div class="single-answer">
    <p class="text-muted">
        Answer by <strong> {{ answer.author }}</strong> 
        on {{ answer.created_at }}
    </p>
    <p>{{ answer.body }}</p>
    <div v-if="isAnswerAuthor()" class="answer-owner">
        <button 
                class="btn btn-sm btn-primary mr-1"
                >Edit
        </button>
        <button 
                class="btn btn-sm btn-danger"
                @click="triggerDeleteAnswer"
                >Delete
        </button>
    </div>
    <hr>
</div>
</template>

<script>
export default {
    name: "AnswerComponent",
    props: {
        answer: {
            type: Object,
            required: true
        },
        requestUser: {
            type: String,
            required: true
        }
    },

    methods: {
        isAnswerAuthor() {
            return this.answer.author === this.requestUser;
        },

        triggerDeleteAnswer() {
            this.$emit("delete-answer", this.answer)
        }
    }
}
</script>

<style>

</style>