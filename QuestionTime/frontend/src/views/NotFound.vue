<template>
  <div class="not-found">
    <div class="container">
      <h1 class="notFound">{{ message }}</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "NotFound",

  data() {
    return {
      message: "404 - Page Not Found!"
    };
  }
};
</script>

<style>
.notFound {
  color: red;
  text-align: center;
}
</style>
