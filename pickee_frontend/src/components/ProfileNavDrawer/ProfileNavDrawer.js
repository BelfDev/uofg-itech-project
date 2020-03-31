import Logo from "@/components/Logo/Logo.vue";
import { mdiAccountBox, mdiCog, mdiFilmstrip, mdiMenu } from "@mdi/js"
import NavDrawerLinks from "@/components/NavDrawerLinks/NavDrawerLinks.vue"

export default {
    name: "ProfileNavDrawer",
    props: ["urls"],
    data: function() {
        return {
            iconMenu: mdiMenu,
            drawer: document.body.classList.contains('desktop') ? true : false,
            links: [
                {
                    name: "Profile",
                    url: this.urls.profile,
                    icon: mdiAccountBox
                },

                {
                    name: "Preferences",
                    url: this.urls.preferences,
                    icon: mdiCog
                },

                {
                    name: "History",
                    url: this.urls.history,
                    icon: mdiFilmstrip
                },
            ]
        }
    },
    components: {
        Logo,
        NavDrawerLinks
    }
};
