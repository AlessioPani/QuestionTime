<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>

<script>
import NavbarComponent from "./components/Navbar";
import { apiService } from "./common/api.service";

export default {
  name: "App",
  components: {
    NavbarComponent
  },
  data() {
    return {
      userUsername: null
    };
  },
  methods: {
    async setUserInfo() {
      await apiService("/api/user/").then(result => {
        this.userUsername = result.username;
        window.localStorage.setItem("username", this.userUsername);
      });
    }
  },
  created() {
    this.setUserInfo();
  }
};
</script>

<style class="css">
body {
  font-family: "Playfair Display", serif;
}

.btn:focus {
  box-shadow: none !important;
}
</style>
