import Logo from "@/components/Logo/Logo.vue";
import { mdiAccountBox, mdiCog, mdiFilmstrip, mdiMenu } from "@mdi/js"
import NavDrawerLinks from "@/components/NavDrawerLinks/NavDrawerLinks.vue"

export default {
    name: "ProfileNavDrawer",
    data: () => ({
        iconMenu: mdiMenu,
        drawer: document.body.classList.contains('desktop') ? true : false,
        links: [
            {
                name: "Profile",
                url: "/profile/",
                icon: mdiAccountBox
            },

            {
                name: "Preferences",
                url: "/preferences/",
                icon: mdiCog
            },

            {
                name: "History",
                url: "/history/",
                icon: mdiFilmstrip
            },
        ]
    }),
    components: {
        Logo,
        NavDrawerLinks
    }
};
