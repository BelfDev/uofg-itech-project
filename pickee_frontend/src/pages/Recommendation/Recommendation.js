import Vue from "vue";
import Recommendation from "./Recommendation.vue";

import vuetify from "@/plugins/vuetify/vuetify";

import "@/assets/styles/app.css";
// import "@/assets/styles/pages/recommendation.css";

Vue.config.productionTip = false;

new Vue({
    vuetify,
    render: h => h(Recommendation)
}).$mount("#recommendation");
