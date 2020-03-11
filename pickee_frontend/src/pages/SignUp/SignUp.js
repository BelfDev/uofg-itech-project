import Vue from "vue";
import SignUp from "./SignUp.vue";

import vuetify from "@/plugins/vuetify/vuetify";

import "@/assets/styles/app.css";
// import "@/assets/styles/pages/signup.css";

Vue.config.productionTip = false;

new Vue({
    vuetify,
    render: h => h(SignUp)
}).$mount("#signup");
