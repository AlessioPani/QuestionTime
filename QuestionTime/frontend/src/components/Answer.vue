<template lang="html">
<div class="single-answer">
    <p class="text-muted">
        Answer by <strong> {{ answer.author }}</strong> 
        on {{ answer.created_at }}
    </p>
    <p>
        {{ answer.body }}
    </p>
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
        }
    },
}
</script>

<style>

</style>