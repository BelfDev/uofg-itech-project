import Vue from "vue";
import ProfilePreferences from "./ProfilePreferences.vue";

import vuetify from "@/plugins/vuetify/vuetify";

import "@/assets/styles/app.css";
// import "@/assets/styles/pages/profile-preferences.css";

Vue.config.productionTip = false;

new Vue({
    vuetify,
    render: h => h(ProfilePreferences)
}).$mount("#preferences");
