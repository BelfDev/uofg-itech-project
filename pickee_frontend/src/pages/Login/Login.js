import Vue from "vue";
import Login from "./Login.vue";

import vuetify from "@/plugins/vuetify/vuetify";
import VueCookies from 'vue-cookies'

Vue.use(VueCookies);

import "@/assets/styles/app.css";
// import "@/assets/styles/pages/login.css";

Vue.config.productionTip = false;

new Vue({
    vuetify,
    render: h => h(Login)
}).$mount("#login");
