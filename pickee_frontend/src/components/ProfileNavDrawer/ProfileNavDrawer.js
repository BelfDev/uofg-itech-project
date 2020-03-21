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
                url: "/profile/", // TODO: get from Django
                icon: mdiAccountBox
            },

            {
                name: "Preferences",
                url: "/preferences/", // TODO: get from Django
                icon: mdiCog
            },

            {
                name: "History",
                url: "/history/", // TODO: get from Django
                icon: mdiFilmstrip
            },
        ]
    }),
    components: {
        Logo,
        NavDrawerLinks
    }
};
