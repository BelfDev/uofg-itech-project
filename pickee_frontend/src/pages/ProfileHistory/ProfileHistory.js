import Vue from "vue";
import ProfileHistory from "./ProfileHistory.vue";

import vuetify from "@/plugins/vuetify/vuetify";
import Responsive from "@/plugins/responsive";

new Responsive();

import "@/assets/styles/app.css";
// import "@/assets/styles/pages/profile-history.css";

Vue.config.productionTip = false;

new Vue({
    vuetify,
    render: h => h(ProfileHistory)
}).$mount("#history");
